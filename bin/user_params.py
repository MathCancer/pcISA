 
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

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}

        param_name1 = Button(description='number_of_invaders', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.number_of_invaders = IntText(
          value=15,
          step=1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='number_of_suppliers', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.number_of_suppliers = IntText(
          value=50,
          step=1,
          style=style, layout=widget_layout)

        param_name3 = Button(description='number_of_scouts', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.number_of_scouts = IntText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='number_of_attackers', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.number_of_attackers = IntText(
          value=50,
          step=1,
          style=style, layout=widget_layout)

        param_name5 = Button(description='invader_max_birth_rate', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.invader_max_birth_rate = FloatText(
          value=0.0028,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name6 = Button(description='invader_max_death_rate', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.invader_max_death_rate = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name7 = Button(description='invader_persistence_time', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.invader_persistence_time = FloatText(
          value=15,
          step=1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='invader_migration_speed', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.invader_migration_speed = FloatText(
          value=0.25,
          step=0.01,
          style=style, layout=widget_layout)

        param_name9 = Button(description='invader_migration_bias', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.invader_migration_bias = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='invader_secretion_rate', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.invader_secretion_rate = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name11 = Button(description='invader_quorum_weight', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.invader_quorum_weight = FloatText(
          value=.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name12 = Button(description='scout_persistence_time', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.scout_persistence_time = FloatText(
          value=15,
          step=1,
          style=style, layout=widget_layout)

        param_name13 = Button(description='scout_migration_speed', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.scout_migration_speed = FloatText(
          value=.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='scout_migration_bias', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.scout_migration_bias = FloatText(
          value=0.125,
          step=0.01,
          style=style, layout=widget_layout)

        param_name15 = Button(description='scout_secretion_rate', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.scout_secretion_rate = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name16 = Button(description='scout_signal_threshold', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.scout_signal_threshold = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name17 = Button(description='attacker_max_birth_rate', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.attacker_max_birth_rate = FloatText(
          value=0.0005,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name18 = Button(description='attacker_max_death_rate', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.attacker_max_death_rate = FloatText(
          value=0.0001,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name19 = Button(description='attacker_persistence_time', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.attacker_persistence_time = FloatText(
          value=15,
          step=1,
          style=style, layout=widget_layout)

        param_name20 = Button(description='attacker_migration_speed', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.attacker_migration_speed = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name21 = Button(description='attacker_migration_bias', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.attacker_migration_bias = FloatText(
          value=0.25,
          step=0.01,
          style=style, layout=widget_layout)

        param_name22 = Button(description='attacker_secretion_rate', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.attacker_secretion_rate = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name23 = Button(description='attacker_signal_threshold', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.attacker_signal_threshold = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name24 = Button(description='supplier_secretion_rate', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'tan'

        self.supplier_secretion_rate = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'
        units_button24 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'tan'

        desc_button1 = Button(description='number of randomly placed invaders', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='number of randomly placed suppliers', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='number of randomly placed scouts', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='number of randomly placed attackers', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='max birth rate for invaders', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='max death rate for invaders', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='persistence time for invader migration', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='speed of invader cells', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='invader migration bias', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='rate invaders secrete their signals', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='motile direction = w*grad(Q) - (1-w)*grad(D)', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='persistence time for scout migration', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='speed of scout cells', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='scout migration bias', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='rate scouts secrete their signals', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='scouts release S if Q > threshold', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='max birth rate for attackers', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='max death rate for attackers', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='persistence time for attacker migration', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='speed of attacker cells', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='attacker migration bias', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='rate attackers secrete their signals', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='attackers release P if S > threshold', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='rate suppliers release resource', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'

        row1 = [param_name1, self.number_of_invaders, units_button1, desc_button1] 
        row2 = [param_name2, self.number_of_suppliers, units_button2, desc_button2] 
        row3 = [param_name3, self.number_of_scouts, units_button3, desc_button3] 
        row4 = [param_name4, self.number_of_attackers, units_button4, desc_button4] 
        row5 = [param_name5, self.invader_max_birth_rate, units_button5, desc_button5] 
        row6 = [param_name6, self.invader_max_death_rate, units_button6, desc_button6] 
        row7 = [param_name7, self.invader_persistence_time, units_button7, desc_button7] 
        row8 = [param_name8, self.invader_migration_speed, units_button8, desc_button8] 
        row9 = [param_name9, self.invader_migration_bias, units_button9, desc_button9] 
        row10 = [param_name10, self.invader_secretion_rate, units_button10, desc_button10] 
        row11 = [param_name11, self.invader_quorum_weight, units_button11, desc_button11] 
        row12 = [param_name12, self.scout_persistence_time, units_button12, desc_button12] 
        row13 = [param_name13, self.scout_migration_speed, units_button13, desc_button13] 
        row14 = [param_name14, self.scout_migration_bias, units_button14, desc_button14] 
        row15 = [param_name15, self.scout_secretion_rate, units_button15, desc_button15] 
        row16 = [param_name16, self.scout_signal_threshold, units_button16, desc_button16] 
        row17 = [param_name17, self.attacker_max_birth_rate, units_button17, desc_button17] 
        row18 = [param_name18, self.attacker_max_death_rate, units_button18, desc_button18] 
        row19 = [param_name19, self.attacker_persistence_time, units_button19, desc_button19] 
        row20 = [param_name20, self.attacker_migration_speed, units_button20, desc_button20] 
        row21 = [param_name21, self.attacker_migration_bias, units_button21, desc_button21] 
        row22 = [param_name22, self.attacker_secretion_rate, units_button22, desc_button22] 
        row23 = [param_name23, self.attacker_signal_threshold, units_button23, desc_button23] 
        row24 = [param_name24, self.supplier_secretion_rate, units_button24, desc_button24] 

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
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
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
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
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
