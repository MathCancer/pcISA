 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        style = {'description_width': '250px'}
        layout = {'width': '400px'}

        self.resource_D = FloatText(
          description='resource_D',
          value=100000,
          step=10000,
          style=style, layout=layout)

        self.resource_lambda = FloatText(
          description='resource_lambda',
          value=0.1,
          step=0.01,
          style=style, layout=layout)

        self.quorum_D = FloatText(
          description='quorum_D',
          value=100000,
          step=10000,
          style=style, layout=layout)

        self.quorum_lambda = FloatText(
          description='quorum_lambda',
          value=10,
          step=1,
          style=style, layout=layout)

        self.death_signal_D = FloatText(
          description='death_signal_D',
          value=40000,
          step=1000,
          style=style, layout=layout)

        self.death_signal_lambda = FloatText(
          description='death_signal_lambda',
          value=1,
          step=0.1,
          style=style, layout=layout)

        self.signal_D = FloatText(
          description='signal_D',
          value=25000,
          step=1000,
          style=style, layout=layout)

        self.signal_lambda = FloatText(
          description='signal_lambda',
          value=.1,
          step=0.01,
          style=style, layout=layout)

        self.poison_D = FloatText(
          description='poison_D',
          value=50000,
          step=1000,
          style=style, layout=layout)

        self.poison_lambda = FloatText(
          description='poison_lambda',
          value=20,
          step=1,
          style=style, layout=layout)

        self.number_of_invaders = IntText(
          description='number_of_invaders',
          value=15,
          step=1,
          style=style, layout=layout)

        self.number_of_suppliers = IntText(
          description='number_of_suppliers',
          value=50,
          step=1,
          style=style, layout=layout)

        self.number_of_scouts = IntText(
          description='number_of_scouts',
          value=10,
          step=1,
          style=style, layout=layout)

        self.number_of_attackers = IntText(
          description='number_of_attackers',
          value=50,
          step=1,
          style=style, layout=layout)

        self.invader_max_birth_rate = FloatText(
          description='invader_max_birth_rate',
          value=0.0028,
          step=0.0001,
          style=style, layout=layout)

        self.invader_max_death_rate = FloatText(
          description='invader_max_death_rate',
          value=0.001,
          step=0.0001,
          style=style, layout=layout)

        self.invader_persistence_time = FloatText(
          description='invader_persistence_time',
          value=15,
          step=1,
          style=style, layout=layout)

        self.invader_migration_speed = FloatText(
          description='invader_migration_speed',
          value=0.25,
          step=0.01,
          style=style, layout=layout)

        self.invader_migration_bias = FloatText(
          description='invader_migration_bias',
          value=0.5,
          step=0.1,
          style=style, layout=layout)

        self.invader_secretion_rate = FloatText(
          description='invader_secretion_rate',
          value=100,
          step=10,
          style=style, layout=layout)

        self.invader_quorum_weight = FloatText(
          description='invader_quorum_weight',
          value=.1,
          step=0.01,
          style=style, layout=layout)

        self.scout_persistence_time = FloatText(
          description='scout_persistence_time',
          value=15,
          step=1,
          style=style, layout=layout)

        self.scout_migration_speed = FloatText(
          description='scout_migration_speed',
          value=.5,
          step=0.1,
          style=style, layout=layout)

        self.scout_migration_bias = FloatText(
          description='scout_migration_bias',
          value=0.125,
          step=0.01,
          style=style, layout=layout)

        self.scout_secretion_rate = FloatText(
          description='scout_secretion_rate',
          value=100,
          step=10,
          style=style, layout=layout)

        self.scout_signal_threshold = FloatText(
          description='scout_signal_threshold',
          value=0.1,
          step=0.01,
          style=style, layout=layout)

        self.attacker_max_birth_rate = FloatText(
          description='attacker_max_birth_rate',
          value=0.0005,
          step=0.0001,
          style=style, layout=layout)

        self.attacker_max_death_rate = FloatText(
          description='attacker_max_death_rate',
          value=0.0001,
          step=1e-05,
          style=style, layout=layout)

        self.attacker_persistence_time = FloatText(
          description='attacker_persistence_time',
          value=15,
          step=1,
          style=style, layout=layout)

        self.attacker_migration_speed = FloatText(
          description='attacker_migration_speed',
          value=1,
          step=0.1,
          style=style, layout=layout)

        self.attacker_migration_bias = FloatText(
          description='attacker_migration_bias',
          value=0.25,
          step=0.01,
          style=style, layout=layout)

        self.attacker_secretion_rate = FloatText(
          description='attacker_secretion_rate',
          value=100,
          step=10,
          style=style, layout=layout)

        self.attacker_signal_threshold = FloatText(
          description='attacker_signal_threshold',
          value=0.1,
          step=0.01,
          style=style, layout=layout)

        self.supplier_secretion_rate = FloatText(
          description='supplier_secretion_rate',
          value=100,
          step=10,
          style=style, layout=layout)

        param_button_layout={'width':'400px'} 

        desc_row1 = Button(description='resource diffusion coefficient', disabled=True, layout=param_button_layout) 
        desc_row1.style.button_color = 'lightgreen'
        desc_row2 = Button(description='resource decay rate', disabled=True, layout=param_button_layout) 
        desc_row2.style.button_color = 'tan'
        desc_row3 = Button(description='quorum diffusion coefficient', disabled=True, layout=param_button_layout) 
        desc_row3.style.button_color = 'lightgreen'
        desc_row4 = Button(description='quorum decay rate', disabled=True, layout=param_button_layout) 
        desc_row4.style.button_color = 'tan'
        desc_row5 = Button(description='death signal diffusion coefficient', disabled=True, layout=param_button_layout) 
        desc_row5.style.button_color = 'lightgreen'
        desc_row6 = Button(description='death signal decay rate', disabled=True, layout=param_button_layout) 
        desc_row6.style.button_color = 'tan'
        desc_row7 = Button(description='attack signal diffusion coefficient', disabled=True, layout=param_button_layout) 
        desc_row7.style.button_color = 'lightgreen'
        desc_row8 = Button(description='attack signal decay rate', disabled=True, layout=param_button_layout) 
        desc_row8.style.button_color = 'tan'
        desc_row9 = Button(description='poison diffusion coefficient', disabled=True, layout=param_button_layout) 
        desc_row9.style.button_color = 'lightgreen'
        desc_row10 = Button(description='poison decay rate', disabled=True, layout=param_button_layout) 
        desc_row10.style.button_color = 'tan'
        desc_row11 = Button(description='number of randomly placed invaders', disabled=True, layout=param_button_layout) 
        desc_row11.style.button_color = 'lightgreen'
        desc_row12 = Button(description='number of randomly placed suppliers', disabled=True, layout=param_button_layout) 
        desc_row12.style.button_color = 'tan'
        desc_row13 = Button(description='number of randomly placed scouts', disabled=True, layout=param_button_layout) 
        desc_row13.style.button_color = 'lightgreen'
        desc_row14 = Button(description='number of randomly placed attackers', disabled=True, layout=param_button_layout) 
        desc_row14.style.button_color = 'tan'
        desc_row15 = Button(description='max birth rate for invaders', disabled=True, layout=param_button_layout) 
        desc_row15.style.button_color = 'lightgreen'
        desc_row16 = Button(description='max death rate for invaders', disabled=True, layout=param_button_layout) 
        desc_row16.style.button_color = 'tan'
        desc_row17 = Button(description='persistence time for invader migration', disabled=True, layout=param_button_layout) 
        desc_row17.style.button_color = 'lightgreen'
        desc_row18 = Button(description='speed of invader cells', disabled=True, layout=param_button_layout) 
        desc_row18.style.button_color = 'tan'
        desc_row19 = Button(description='invader migration bias', disabled=True, layout=param_button_layout) 
        desc_row19.style.button_color = 'lightgreen'
        desc_row20 = Button(description='rate invaders secrete their signals', disabled=True, layout=param_button_layout) 
        desc_row20.style.button_color = 'tan'
        desc_row21 = Button(description='motile direction = w*grad(Q) - (1-w)*grad(D)', disabled=True, layout=param_button_layout) 
        desc_row21.style.button_color = 'lightgreen'
        desc_row22 = Button(description='persistence time for scout migration', disabled=True, layout=param_button_layout) 
        desc_row22.style.button_color = 'tan'
        desc_row23 = Button(description='speed of scout cells', disabled=True, layout=param_button_layout) 
        desc_row23.style.button_color = 'lightgreen'
        desc_row24 = Button(description='scout migration bias', disabled=True, layout=param_button_layout) 
        desc_row24.style.button_color = 'tan'
        desc_row25 = Button(description='rate scouts secrete their signals', disabled=True, layout=param_button_layout) 
        desc_row25.style.button_color = 'lightgreen'
        desc_row26 = Button(description='scouts release S if Q > threshold', disabled=True, layout=param_button_layout) 
        desc_row26.style.button_color = 'tan'
        desc_row27 = Button(description='max birth rate for attackers', disabled=True, layout=param_button_layout) 
        desc_row27.style.button_color = 'lightgreen'
        desc_row28 = Button(description='max death rate for attackers', disabled=True, layout=param_button_layout) 
        desc_row28.style.button_color = 'tan'
        desc_row29 = Button(description='persistence time for attacker migration', disabled=True, layout=param_button_layout) 
        desc_row29.style.button_color = 'lightgreen'
        desc_row30 = Button(description='speed of attacker cells', disabled=True, layout=param_button_layout) 
        desc_row30.style.button_color = 'tan'
        desc_row31 = Button(description='attacker migration bias', disabled=True, layout=param_button_layout) 
        desc_row31.style.button_color = 'lightgreen'
        desc_row32 = Button(description='rate attackers secrete their signals', disabled=True, layout=param_button_layout) 
        desc_row32.style.button_color = 'tan'
        desc_row33 = Button(description='attackers release P if S > threshold', disabled=True, layout=param_button_layout) 
        desc_row33.style.button_color = 'lightgreen'
        desc_row34 = Button(description='rate suppliers release resource', disabled=True, layout=param_button_layout) 
        desc_row34.style.button_color = 'tan'

        row1 = [self.resource_D, Label('micron^2/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row1] 
        row2 = [self.resource_lambda, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row2] 
        row3 = [self.quorum_D, Label('micron^2/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row3] 
        row4 = [self.quorum_lambda, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row4] 
        row5 = [self.death_signal_D, Label('micron^2/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row5] 
        row6 = [self.death_signal_lambda, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row6] 
        row7 = [self.signal_D, Label('micron^2/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row7] 
        row8 = [self.signal_lambda, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row8] 
        row9 = [self.poison_D, Label('micron^2/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row9] 
        row10 = [self.poison_lambda, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row10] 
        row11 = [self.number_of_invaders, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row11] 
        row12 = [self.number_of_suppliers, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row12] 
        row13 = [self.number_of_scouts, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row13] 
        row14 = [self.number_of_attackers, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row14] 
        row15 = [self.invader_max_birth_rate, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row15] 
        row16 = [self.invader_max_death_rate, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row16] 
        row17 = [self.invader_persistence_time, Label('min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row17] 
        row18 = [self.invader_migration_speed, Label('micron/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row18] 
        row19 = [self.invader_migration_bias, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row19] 
        row20 = [self.invader_secretion_rate, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row20] 
        row21 = [self.invader_quorum_weight, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row21] 
        row22 = [self.scout_persistence_time, Label('min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row22] 
        row23 = [self.scout_migration_speed, Label('micron/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row23] 
        row24 = [self.scout_migration_bias, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row24] 
        row25 = [self.scout_secretion_rate, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row25] 
        row26 = [self.scout_signal_threshold, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row26] 
        row27 = [self.attacker_max_birth_rate, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row27] 
        row28 = [self.attacker_max_death_rate, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row28] 
        row29 = [self.attacker_persistence_time, Label('min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row29] 
        row30 = [self.attacker_migration_speed, Label('micron/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row30] 
        row31 = [self.attacker_migration_bias, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row31] 
        row32 = [self.attacker_secretion_rate, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row32] 
        row33 = [self.attacker_signal_threshold, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row33] 
        row34 = [self.supplier_secretion_rate, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row34] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          box26,
          box27,
          box28,
          box29,
          box30,
          box31,
          box32,
          box33,
          box34,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.resource_D.value = float(uep.find('.//resource_D').text)
        self.resource_lambda.value = float(uep.find('.//resource_lambda').text)
        self.quorum_D.value = float(uep.find('.//quorum_D').text)
        self.quorum_lambda.value = float(uep.find('.//quorum_lambda').text)
        self.death_signal_D.value = float(uep.find('.//death_signal_D').text)
        self.death_signal_lambda.value = float(uep.find('.//death_signal_lambda').text)
        self.signal_D.value = float(uep.find('.//signal_D').text)
        self.signal_lambda.value = float(uep.find('.//signal_lambda').text)
        self.poison_D.value = float(uep.find('.//poison_D').text)
        self.poison_lambda.value = float(uep.find('.//poison_lambda').text)
        self.number_of_invaders.value = int(uep.find('.//number_of_invaders').text)
        self.number_of_suppliers.value = int(uep.find('.//number_of_suppliers').text)
        self.number_of_scouts.value = int(uep.find('.//number_of_scouts').text)
        self.number_of_attackers.value = int(uep.find('.//number_of_attackers').text)
        self.invader_max_birth_rate.value = float(uep.find('.//invader_max_birth_rate').text)
        self.invader_max_death_rate.value = float(uep.find('.//invader_max_death_rate').text)
        self.invader_persistence_time.value = float(uep.find('.//invader_persistence_time').text)
        self.invader_migration_speed.value = float(uep.find('.//invader_migration_speed').text)
        self.invader_migration_bias.value = float(uep.find('.//invader_migration_bias').text)
        self.invader_secretion_rate.value = float(uep.find('.//invader_secretion_rate').text)
        self.invader_quorum_weight.value = float(uep.find('.//invader_quorum_weight').text)
        self.scout_persistence_time.value = float(uep.find('.//scout_persistence_time').text)
        self.scout_migration_speed.value = float(uep.find('.//scout_migration_speed').text)
        self.scout_migration_bias.value = float(uep.find('.//scout_migration_bias').text)
        self.scout_secretion_rate.value = float(uep.find('.//scout_secretion_rate').text)
        self.scout_signal_threshold.value = float(uep.find('.//scout_signal_threshold').text)
        self.attacker_max_birth_rate.value = float(uep.find('.//attacker_max_birth_rate').text)
        self.attacker_max_death_rate.value = float(uep.find('.//attacker_max_death_rate').text)
        self.attacker_persistence_time.value = float(uep.find('.//attacker_persistence_time').text)
        self.attacker_migration_speed.value = float(uep.find('.//attacker_migration_speed').text)
        self.attacker_migration_bias.value = float(uep.find('.//attacker_migration_bias').text)
        self.attacker_secretion_rate.value = float(uep.find('.//attacker_secretion_rate').text)
        self.attacker_signal_threshold.value = float(uep.find('.//attacker_signal_threshold').text)
        self.supplier_secretion_rate.value = float(uep.find('.//supplier_secretion_rate').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//resource_D').text = str(self.resource_D.value)
        uep.find('.//resource_lambda').text = str(self.resource_lambda.value)
        uep.find('.//quorum_D').text = str(self.quorum_D.value)
        uep.find('.//quorum_lambda').text = str(self.quorum_lambda.value)
        uep.find('.//death_signal_D').text = str(self.death_signal_D.value)
        uep.find('.//death_signal_lambda').text = str(self.death_signal_lambda.value)
        uep.find('.//signal_D').text = str(self.signal_D.value)
        uep.find('.//signal_lambda').text = str(self.signal_lambda.value)
        uep.find('.//poison_D').text = str(self.poison_D.value)
        uep.find('.//poison_lambda').text = str(self.poison_lambda.value)
        uep.find('.//number_of_invaders').text = str(self.number_of_invaders.value)
        uep.find('.//number_of_suppliers').text = str(self.number_of_suppliers.value)
        uep.find('.//number_of_scouts').text = str(self.number_of_scouts.value)
        uep.find('.//number_of_attackers').text = str(self.number_of_attackers.value)
        uep.find('.//invader_max_birth_rate').text = str(self.invader_max_birth_rate.value)
        uep.find('.//invader_max_death_rate').text = str(self.invader_max_death_rate.value)
        uep.find('.//invader_persistence_time').text = str(self.invader_persistence_time.value)
        uep.find('.//invader_migration_speed').text = str(self.invader_migration_speed.value)
        uep.find('.//invader_migration_bias').text = str(self.invader_migration_bias.value)
        uep.find('.//invader_secretion_rate').text = str(self.invader_secretion_rate.value)
        uep.find('.//invader_quorum_weight').text = str(self.invader_quorum_weight.value)
        uep.find('.//scout_persistence_time').text = str(self.scout_persistence_time.value)
        uep.find('.//scout_migration_speed').text = str(self.scout_migration_speed.value)
        uep.find('.//scout_migration_bias').text = str(self.scout_migration_bias.value)
        uep.find('.//scout_secretion_rate').text = str(self.scout_secretion_rate.value)
        uep.find('.//scout_signal_threshold').text = str(self.scout_signal_threshold.value)
        uep.find('.//attacker_max_birth_rate').text = str(self.attacker_max_birth_rate.value)
        uep.find('.//attacker_max_death_rate').text = str(self.attacker_max_death_rate.value)
        uep.find('.//attacker_persistence_time').text = str(self.attacker_persistence_time.value)
        uep.find('.//attacker_migration_speed').text = str(self.attacker_migration_speed.value)
        uep.find('.//attacker_migration_bias').text = str(self.attacker_migration_bias.value)
        uep.find('.//attacker_secretion_rate').text = str(self.attacker_secretion_rate.value)
        uep.find('.//attacker_signal_threshold').text = str(self.attacker_signal_threshold.value)
        uep.find('.//supplier_secretion_rate').text = str(self.supplier_secretion_rate.value)
