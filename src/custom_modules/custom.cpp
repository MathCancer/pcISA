/*
###############################################################################
# If you use PhysiCell in your project, please cite PhysiCell and the version #
# number, such as below:                                                      #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1].    #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# See VERSION.txt or call get_PhysiCell_version() to get the current version  #
#     x.y.z. Call display_citations() to get detailed information on all cite-#
#     able software used in your PhysiCell application.                       #
#                                                                             #
# Because PhysiCell extensively uses BioFVM, we suggest you also cite BioFVM  #
#     as below:                                                               #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1],    #
# with BioFVM [2] to solve the transport equations.                           #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# [2] A Ghaffarizadeh, SH Friedman, and P Macklin, BioFVM: an efficient para- #
#     llelized diffusive transport solver for 3-D biological simulations,     #
#     Bioinformatics 32(8): 1256-8, 2016. DOI: 10.1093/bioinformatics/btv730  #
#                                                                             #
###############################################################################
#                                                                             #
# BSD 3-Clause License (see https://opensource.org/licenses/BSD-3-Clause)     #
#                                                                             #
# Copyright (c) 2015-2018, Paul Macklin and the PhysiCell Project             #
# All rights reserved.                                                        #
#                                                                             #
# Redistribution and use in source and binary forms, with or without          #
# modification, are permitted provided that the following conditions are met: #
#                                                                             #
# 1. Redistributions of source code must retain the above copyright notice,   #
# this list of conditions and the following disclaimer.                       #
#                                                                             #
# 2. Redistributions in binary form must reproduce the above copyright        #
# notice, this list of conditions and the following disclaimer in the         #
# documentation and/or other materials provided with the distribution.        #
#                                                                             #
# 3. Neither the name of the copyright holder nor the names of its            #
# contributors may be used to endorse or promote products derived from this   #
# software without specific prior written permission.                         #
#                                                                             #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE   #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE  #
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE   #
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF        #
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS    #
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN     #
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)     #
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE  #
# POSSIBILITY OF SUCH DAMAGE.                                                 #
#                                                                             #
###############################################################################
*/

#include "./custom.h"

// declare cell definitions here 

Cell_Definition invader; 
Cell_Definition scout; 
Cell_Definition attacker; 
Cell_Definition supplier; 

void create_cell_types( void )
{
	// use the same random seed so that future experiments have the 
	// same initial histogram of oncoprotein, even if threading means 
	// that future division and other events are still not identical 
	// for all runs 
	
	SeedRandom( parameters.ints("random_seed") ); // or specify a seed here 
	
	// housekeeping 
	
	initialize_default_cell_definition();
	cell_defaults.phenotype.secretion.sync_to_microenvironment( &microenvironment ); 
	
	// Name the default cell type 
	
	cell_defaults.type = -1; 
	cell_defaults.name = "default"; 
	
	// set default cell cycle model 

	cell_defaults.functions.cycle_model = live; 
	
	// set default_cell_functions; 
	
	cell_defaults.functions.update_phenotype = NULL; 
	
	// needed for a 2-D simulation: 
	
	/* grab code from heterogeneity */ 
	
	cell_defaults.functions.set_orientation = up_orientation; 
	cell_defaults.phenotype.geometry.polarity = 1.0;
	cell_defaults.phenotype.motility.restrict_to_2D = true; 
	
	// make sure the defaults are self-consistent. 
	
	cell_defaults.phenotype.secretion.sync_to_microenvironment( &microenvironment );
	cell_defaults.phenotype.sync_to_functions( cell_defaults.functions ); 

	// set the rate terms in the default phenotype 

	// first find index for a few key variables. 
	int apoptosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "Apoptosis" );
	int necrosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "Necrosis" );

	int start_index = live.find_phase_index( PhysiCell_constants::live );
	int end_index = live.find_phase_index( PhysiCell_constants::live );
	
	int R_i = microenvironment.find_density_index( "resource" ); 
	int S_i = microenvironment.find_density_index( "signal" ); 
	int DS_i = microenvironment.find_density_index( "death signal" ); 
	int P_i = microenvironment.find_density_index( "poison" ); 
	int Q_i = microenvironment.find_density_index( "quorum" ); 

	// initially no death 
	cell_defaults.phenotype.death.rates[apoptosis_model_index] = 0.0; 
	cell_defaults.phenotype.death.rates[necrosis_model_index] = 0.0; 
	// initially no birth
	cell_defaults.phenotype.cycle.data.transition_rate( start_index , end_index ) = 0.0; 

	// set all secretion and uptake off 
	cell_defaults.phenotype.secretion.set_all_secretion_to_zero(); 
	cell_defaults.phenotype.secretion.set_all_uptake_to_zero(); 
	
	// set motility on
	cell_defaults.phenotype.motility.is_motile = true;  
	cell_defaults.phenotype.motility.migration_bias = 0; 
	cell_defaults.phenotype.motility.migration_speed = 1.0; 
	cell_defaults.phenotype.motility.persistence_time = 10.0; 
	
	// add custom data here, if any 

	/* invader setup */ 
	invader = cell_defaults;
	invader.type = 0; 
	invader.name = "invader"; 
	invader.parameters.pReference_live_phenotype = &( invader.phenotype ); 
	
	invader.functions.update_phenotype = invader_rule;
	invader.functions.update_migration_bias = invader_migration_rule; 
	
	invader.phenotype.secretion.secretion_rates[Q_i] = 
		parameters.doubles("invader_secretion_rate" ); 
	invader.phenotype.secretion.saturation_densities[Q_i] = 1.0; 
	invader.phenotype.secretion.uptake_rates[R_i] = 10.0; 
	invader.phenotype.motility.migration_speed = 
		parameters.doubles( "invader_migration_speed" ); 
	invader.phenotype.motility.migration_bias = 
		parameters.doubles( "invader_migration_bias" ); 
	invader.phenotype.motility.persistence_time = 
		parameters.doubles( "invader_persistence_time" ); 

	/* attacker setup */ 	
	attacker = cell_defaults;
	attacker.type = 1; 
	attacker.name = "attacker"; 
	attacker.parameters.pReference_live_phenotype = &( attacker.phenotype ); 
	
	attacker.functions.update_phenotype = attacker_rule; 
	attacker.functions.update_migration_bias = attacker_migration_rule; 
	
	attacker.phenotype.secretion.saturation_densities[P_i] = 1.0; 
	
	attacker.phenotype.motility.migration_speed = 
		parameters.doubles( "attacker_migration_speed" ); 
	attacker.phenotype.motility.migration_bias = 
		parameters.doubles( "attacker_migration_bias" ); 
	attacker.phenotype.motility.persistence_time = 
		parameters.doubles( "attacker_persistence_time" ); 

	/* scout setup */ 
	scout = cell_defaults;
	scout.type = 2; 
	scout.name = "scout"; 
	scout.parameters.pReference_live_phenotype = &( scout.phenotype ); 

	scout.functions.update_phenotype = scout_rule; 
	scout.functions.update_migration_bias = scout_migration_rule; 
	scout.phenotype.secretion.saturation_densities[S_i] = 1.0; 
	
	scout.phenotype.motility.migration_speed = 
		parameters.doubles( "scout_migration_speed" ); 
	scout.phenotype.motility.migration_bias = 
		parameters.doubles( "scout_migration_bias" ); 
	scout.phenotype.motility.persistence_time = 
		parameters.doubles( "scout_persistence_time" ); 
		
	/* supplier setup */ 
	
	supplier = cell_defaults;
	supplier.type = 3; 
	supplier.name = "supplier"; 
	supplier.parameters.pReference_live_phenotype = &( supplier.phenotype ); 
	
	// turn on source of resource
	supplier.phenotype.secretion.secretion_rates[ R_i ] = 
		parameters.doubles( "supplier_secretion_rate" ); 
	supplier.phenotype.secretion.saturation_densities[ R_i ] = 1.0; 
	// turn off motility 
	supplier.phenotype.motility.is_motile = false;
	// disable volume updates 
	supplier.functions.volume_update_function = NULL; 
	// don't forget to set each individual to unmovable 
	// and set total volume to dx * dy * dz 
	
	return; 
}

void setup_microenvironment( void )
{
	// set domain parameters 
	
/* now this is in XML 
	default_microenvironment_options.X_range = {-1000, 1000}; 
	default_microenvironment_options.Y_range = {-1000, 1000}; 
	default_microenvironment_options.simulate_2D = true; 
*/
	// make sure to override and go back to 2D 
	if( default_microenvironment_options.simulate_2D == false )
	{
		std::cout << "Warning: overriding XML config option and setting to 2D!" << std::endl; 
		default_microenvironment_options.simulate_2D = true; 
	}
	
	int index = 0; 
	default_microenvironment_options.use_oxygen_as_first_field = false; 
	Microenvironment* pME = get_default_microenvironment(); 
	pME->set_density( index , "resource", "dimensionless" ); 
	pME->diffusion_coefficients[index] = parameters.doubles("resource_D"); 
	pME->decay_rates[index] = parameters.doubles("resource_lambda"); 
	index++;
	
	pME->add_density( "quorum" ,"dimensionless" ); 
	pME->diffusion_coefficients[index] = parameters.doubles("quorum_D"); 
	pME->decay_rates[index] = parameters.doubles("quorum_lambda"); 
	index++; 
	
	pME->add_density( "death signal" ,"dimensionless" ); 
	pME->diffusion_coefficients[index] = parameters.doubles("death_signal_D"); 
	pME->decay_rates[index] = parameters.doubles("death_signal_lambda"); 
	index++; 

	pME->add_density( "signal" ,"dimensionless" ); 
	pME->diffusion_coefficients[index] = parameters.doubles("signal_D"); 
	pME->decay_rates[index] = parameters.doubles("signal_lambda"); 
	index++; 
	
	pME->add_density( "poison" ,"dimensionless" ); 
	pME->diffusion_coefficients[index] = parameters.doubles("poison_D"); 
	pME->decay_rates[index] = parameters.doubles("poison_lambda"); 
	index++; 


	// no gradients need for this example 

	default_microenvironment_options.calculate_gradients = true; 
	
	// set Dirichlet conditions 

	default_microenvironment_options.outer_Dirichlet_conditions = false;
	
	// set boundary condition vector anyway -- used for initial conditions 
	
	std::vector<double> bc_vector = { 1, 0, 0, 0, 0 }; 
	default_microenvironment_options.Dirichlet_condition_vector = bc_vector;
	
	// initialize BioFVM 
	
	initialize_microenvironment(); 	
	
	return; 
}

void setup_tissue( void )
{
	// create some cells near the origin
	
	Cell* pC;
	double width = default_microenvironment_options.X_range[1] -
		default_microenvironment_options.X_range[0]; 
	double height = default_microenvironment_options.Y_range[1] -
		default_microenvironment_options.Y_range[0]; 

	// seed invaders
	for( int n=0; n < parameters.ints("number_of_invaders") ; n++ )
	{
		pC = create_cell(invader); 
		std::vector<double> position = {0,0,0}; 
		position[0] = default_microenvironment_options.X_range[0] + 20 + 
			(width-40.0)*UniformRandom(); 
		position[1] = default_microenvironment_options.Y_range[0] + 20 + 
			(height-40.0)*UniformRandom(); 
		pC->assign_position( position ); 
	}

	// seed suppliers 
	for( int n=0; n < parameters.ints("number_of_suppliers") ; n++ )
	{
		pC = create_cell(supplier); 
		std::vector<double> position = {0,0,0}; 
		position[0] = default_microenvironment_options.X_range[0] + 20 + 
			(width-40.0)*UniformRandom(); 
		position[1] = default_microenvironment_options.Y_range[0] + 20 + 
			(height-40.0)*UniformRandom(); 
		pC->assign_position( position ); 
		pC->is_movable = false; 
		pC->set_total_volume( 20*20*20 ); 
	}
	
	// seed scouts 
	for( int n=0; n < parameters.ints("number_of_scouts") ; n++ )
	{
		pC = create_cell(scout); 
		std::vector<double> position = {0,0,0}; 
		position[0] = default_microenvironment_options.X_range[0] + 20 + 
			(width-40.0)*UniformRandom(); 
		position[1] = default_microenvironment_options.Y_range[0] + 20 + 
			(height-40.0)*UniformRandom(); 
		pC->assign_position( position ); 
	}
	
	// seed attackers 
	for( int n=0; n < parameters.ints("number_of_attackers") ; n++ )
	{
		pC = create_cell(attacker); 
		std::vector<double> position = {0,0,0}; 
		position[0] = default_microenvironment_options.X_range[0] + 20 + 
			(width-40.0)*UniformRandom(); 
		position[1] = default_microenvironment_options.Y_range[0] + 20 + 
			(height-40.0)*UniformRandom(); 
		pC->assign_position( position ); 
	}
	
	return; 
}

std::vector<std::string> my_coloring_function( Cell* pCell )
{
	// start with flow cytometry coloring 
	
	std::vector<std::string> output = false_cell_coloring_cytometry(pCell); 
		
	if( pCell->phenotype.death.dead == false && pCell->type == 1 )
	{
		 output[0] = "black"; 
		 output[2] = "black"; 
	}
	
	return output; 
}

std::vector<std::string> paint_by_numbers( Cell* pCell )
{
	std::vector<std::string> output( 4, "black" );
	std::string color = "white";
	
	if( pCell->type == 0 )
	{
		color = "red";
		if( pCell->phenotype.death.dead == true )
		{ color = "darkred"; }
	}
	
	if( pCell->type == 1 )
	{
		color = "blue";
		if( pCell->phenotype.death.dead == true )
		{ color = "darkblue"; }
	}
	
	if( pCell->type == 2 )
	{
		color = "green";
		if( pCell->phenotype.death.dead == true )
		{ color = "darkgreen"; }
	}
	
	if( pCell->type == 3 )
	{
		color = "yellow";
		if( pCell->phenotype.death.dead == true )
		{ color = "goldenrod"; } // no dark yellow 
	}
	
	if( pCell->type == 4 )
	{
		color = "orange";
		if( pCell->phenotype.death.dead == true )
		{ color = "darkorange"; }
	}
	
	if( pCell->type == 5 )
	{
		color = "magenta";
		if( pCell->phenotype.death.dead == true )
		{ color = "darkmagenta"; }
	}
	
	if( pCell->type == 6 )
	{
		color = "cyan";
		if( pCell->phenotype.death.dead == true )
		{ color = "darkcyan"; }
	}

	if( pCell->type == 7 )
	{
		color = "gray";
		if( pCell->phenotype.death.dead == true )
		{ color = "darkgrey"; }
	}
	
	output[0] = color; 
	output[2] = color; 
	output[3] = color; 	
	return output; 
}

void invader_rule( Cell* pCell, Phenotype& phenotype , double dt )
{
	// find the correct models, phase indices, substrates, etc.
	static int apoptosis_model_index = phenotype.death.find_death_model_index( "Apoptosis" );
	static int necrosis_model_index = phenotype.death.find_death_model_index( "Necrosis" );

	static int start_index = live.find_phase_index( PhysiCell_constants::live );
	static int end_index = live.find_phase_index( PhysiCell_constants::live );
	
	static int quorum_index = microenvironment.find_density_index( "quorum" ); 
	static int resource_index = microenvironment.find_density_index( "resource" ); 
	static int death_signal_index = microenvironment.find_density_index( "death signal" ); 
	static int signal_index = microenvironment.find_density_index( "signal" ); 
	static int poison_index = microenvironment.find_density_index( "poison" ); 
	
	static double secretion_rate = parameters.doubles( "invader_secretion_rate" ); 
	
	static double max_birth_rate = parameters.doubles( "invader_max_birth_rate" );
	static double max_death_rate = parameters.doubles( "invader_max_death_rate" ); 

	// if I'm dead, give up 
	if( phenotype.death.dead == true )
	{
		// turn off all secretion 
		phenotype.secretion.set_all_secretion_to_zero(); 
		phenotype.secretion.set_all_uptake_to_zero(); 	

		// release death signal 
		phenotype.secretion.secretion_rates[death_signal_index] = secretion_rate;
		phenotype.secretion.saturation_densities[death_signal_index] = 1.0; 
		
		// stop future evaluations of this function 
		pCell->functions.update_phenotype = NULL; 
		return; 
	}

	// sample resource, poison 
	double R = pCell->nearest_density_vector()[resource_index]; 
	double P = pCell->nearest_density_vector()[poison_index]; 
	double Q = pCell->nearest_density_vector()[quorum_index]; 
	
	phenotype.cycle.data.transition_rate( start_index , end_index ) = 
		R*(1-Q)*max_birth_rate; 
	
	phenotype.death.rates[ apoptosis_model_index ] =  
		(1.0-R+P)*max_death_rate; 

	return; 
}

void invader_migration_rule( Cell* pCell , Phenotype& phenotype , double dt )
{
	static int death_index = microenvironment.find_density_index( "death signal" ); 
	static int quorum_index = microenvironment.find_density_index( "quorum" ); 

	static double weight = parameters.doubles( "invader_quorum_weight" ); 
	static double one_minus_weight = 1.0 - weight; 
	static double neg_one_minus_weight = - one_minus_weight; 
	
	phenotype.motility.migration_bias_direction = pCell->nearest_gradient(quorum_index); // grad(Q)
	phenotype.motility.migration_bias_direction *= weight; // w*grad(Q); 
	
	axpy( &phenotype.motility.migration_bias_direction , neg_one_minus_weight , pCell->nearest_gradient(death_index) ); 
	// w*grad(Q) - (1-w)*grad(D)
	// uses a higher-performance BLAS operation from BioFVM  axpy( *y, a, x) is y = y+a*x 
	
	normalize( &( phenotype.motility.migration_bias_direction ) );
	
	return; 
}


void scout_rule( Cell* pCell , Phenotype& phenotype , double dt )
{
	// find the correct models, phase indices, substrates, etc.
	static int apoptosis_model_index = phenotype.death.find_death_model_index( "Apoptosis" );
	static int necrosis_model_index = phenotype.death.find_death_model_index( "Necrosis" );

	static int start_index = live.find_phase_index( PhysiCell_constants::live );
	static int end_index = live.find_phase_index( PhysiCell_constants::live );
	
	static int quorum_index = microenvironment.find_density_index( "quorum" ); 
	static int resource_index = microenvironment.find_density_index( "resource" ); 
	static int death_signal_index = microenvironment.find_density_index( "death signal" ); 
	static int signal_index = microenvironment.find_density_index( "signal" ); 
	static int poison_index = microenvironment.find_density_index( "poison" ); 
	
	static double secretion_rate = parameters.doubles( "scout_secretion_rate" ); 
	static double threshold = parameters.doubles( "scout_signal_threshold" );  
	
	double Q = pCell->nearest_density_vector()[quorum_index]; 
	if( Q > threshold )
	{
		phenotype.secretion.secretion_rates[ signal_index ] = secretion_rate; 
	}
	else
	{
		phenotype.secretion.secretion_rates[ signal_index ] = 0; 
	}

	return; 
}

void scout_migration_rule( Cell* pCell , Phenotype& phenotype , double dt )
{
	static int quorum_index = microenvironment.find_density_index( "quorum" ); 
	
	phenotype.motility.migration_bias_direction = pCell->nearest_gradient(quorum_index);
	normalize( &( phenotype.motility.migration_bias_direction ) );
	
	return; 
}

void attacker_rule( Cell* pCell , Phenotype& phenotype , double dt )
{
	static int signal_index = microenvironment.find_density_index( "signal" ); 
	
	double S = pCell->nearest_density_vector()[ signal_index ]; 
	
	static int start_index = phenotype.cycle.model().find_phase_index( PhysiCell_constants::live ); 
	static int end_index = phenotype.cycle.model().find_phase_index( PhysiCell_constants::live ); 
	
	static int apoptosis_model_index = 
		phenotype.death.find_death_model_index( "Apoptosis" ); 
	
	static double max_birth_rate = parameters.doubles( "attacker_max_birth_rate" ); 
	static double max_death_rate = parameters.doubles( "attacker_max_death_rate" );
	
	static int poison_index = microenvironment.find_density_index( "poison" ); 
	
	static double secretion_rate = parameters.doubles("attacker_secretion_rate"); 
	static double threshold = parameters.doubles("attacker_signal_threshold"); 
	
	// birth rate increases wiht signal 
	
	phenotype.cycle.data.transition_rate( start_index , end_index ) = 
		S * max_birth_rate; 
	
	// death rate increases with 1-signal 
	
	phenotype.death.rates[ apoptosis_model_index ] = 
		(1-S) * max_death_rate; 
		
	// increase poison secretion with signal 
	
	if( S > threshold )
	{
		phenotype.secretion.secretion_rates[ poison_index ] = secretion_rate; 
	}
	else
	{
		phenotype.secretion.secretion_rates[ poison_index ] = 0; 
	}
	
	return; 
}


void attacker_migration_rule( Cell* pCell , Phenotype& phenotype , double dt )
{
	static int signal_index = microenvironment.find_density_index( "signal" ); 
	
	phenotype.motility.migration_bias_direction = pCell->nearest_gradient(signal_index);
	normalize( &( phenotype.motility.migration_bias_direction ) );
	
	return; 
}

