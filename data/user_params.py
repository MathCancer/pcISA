 
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

        param_name1 = Button(description='resource_D', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.resource_D = FloatText(
          value=100000,
          step=10000,
          style=style, layout=widget_layout)

        param_name2 = Button(description='resource_lambda', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.resource_lambda = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name3 = Button(description='quorum_D', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.quorum_D = FloatText(
          value=100000,
          step=10000,
          style=style, layout=widget_layout)

        param_name4 = Button(description='quorum_lambda', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.quorum_lambda = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name5 = Button(description='death_signal_D', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.death_signal_D = FloatText(
          value=40000,
          step=1000,
          style=style, layout=widget_layout)

        param_name6 = Button(description='death_signal_lambda', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.death_signal_lambda = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='signal_D', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.signal_D = FloatText(
          value=25000,
          step=1000,
          style=style, layout=widget_layout)

        param_name8 = Button(description='signal_lambda', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.signal_lambda = FloatText(
          value=.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name9 = Button(description='poison_D', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.poison_D = FloatText(
          value=50000,
          step=1000,
          style=style, layout=widget_layout)

        param_name10 = Button(description='poison_lambda', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.poison_lambda = FloatText(
          value=20,
          step=1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='number_of_invaders', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.number_of_invaders = IntText(
          value=15,
          step=1,
          style=style, layout=widget_layout)

        param_name12 = Button(description='number_of_suppliers', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.number_of_suppliers = IntText(
          value=50,
          step=1,
          style=style, layout=widget_layout)

        param_name13 = Button(description='number_of_scouts', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.number_of_scouts = IntText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='number_of_attackers', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.number_of_attackers = IntText(
          value=50,
          step=1,
          style=style, layout=widget_layout)

        param_name15 = Button(description='invader_max_birth_rate', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.invader_max_birth_rate = FloatText(
          value=0.0028,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name16 = Button(description='invader_max_death_rate', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.invader_max_death_rate = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name17 = Button(description='invader_persistence_time', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.invader_persistence_time = FloatText(
          value=15,
          step=1,
          style=style, layout=widget_layout)

        param_name18 = Button(description='invader_migration_speed', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.invader_migration_speed = FloatText(
          value=0.25,
          step=0.01,
          style=style, layout=widget_layout)

        param_name19 = Button(description='invader_migration_bias', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.invader_migration_bias = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name20 = Button(description='invader_secretion_rate', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.invader_secretion_rate = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name21 = Button(description='invader_quorum_weight', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.invader_quorum_weight = FloatText(
          value=.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name22 = Button(description='scout_persistence_time', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.scout_persistence_time = FloatText(
          value=15,
          step=1,
          style=style, layout=widget_layout)

        param_name23 = Button(description='scout_migration_speed', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.scout_migration_speed = FloatText(
          value=.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name24 = Button(description='scout_migration_bias', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'tan'

        self.scout_migration_bias = FloatText(
          value=0.125,
          step=0.01,
          style=style, layout=widget_layout)

        param_name25 = Button(description='scout_secretion_rate', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'lightgreen'

        self.scout_secretion_rate = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name26 = Button(description='scout_signal_threshold', disabled=True, layout=name_button_layout)
        param_name26.style.button_color = 'tan'

        self.scout_signal_threshold = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name27 = Button(description='attacker_max_birth_rate', disabled=True, layout=name_button_layout)
        param_name27.style.button_color = 'lightgreen'

        self.attacker_max_birth_rate = FloatText(
          value=0.0005,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name28 = Button(description='attacker_max_death_rate', disabled=True, layout=name_button_layout)
        param_name28.style.button_color = 'tan'

        self.attacker_max_death_rate = FloatText(
          value=0.0001,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name29 = Button(description='attacker_persistence_time', disabled=True, layout=name_button_layout)
        param_name29.style.button_color = 'lightgreen'

        self.attacker_persistence_time = FloatText(
          value=15,
          step=1,
          style=style, layout=widget_layout)

        param_name30 = Button(description='attacker_migration_speed', disabled=True, layout=name_button_layout)
        param_name30.style.button_color = 'tan'

        self.attacker_migration_speed = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name31 = Button(description='attacker_migration_bias', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'lightgreen'

        self.attacker_migration_bias = FloatText(
          value=0.25,
          step=0.01,
          style=style, layout=widget_layout)

        param_name32 = Button(description='attacker_secretion_rate', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'tan'

        self.attacker_secretion_rate = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name33 = Button(description='attacker_signal_threshold', disabled=True, layout=name_button_layout)
        param_name33.style.button_color = 'lightgreen'

        self.attacker_signal_threshold = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name34 = Button(description='supplier_secretion_rate', disabled=True, layout=name_button_layout)
        param_name34.style.button_color = 'tan'

        self.supplier_secretion_rate = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        units_button1 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'
        units_button24 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'tan'
        units_button25 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'lightgreen'
        units_button26 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'tan'
        units_button27 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'lightgreen'
        units_button28 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'tan'
        units_button29 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'lightgreen'
        units_button30 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'tan'
        units_button31 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button31.style.button_color = 'lightgreen'
        units_button32 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button32.style.button_color = 'tan'
        units_button33 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button33.style.button_color = 'lightgreen'
        units_button34 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button34.style.button_color = 'tan'

        desc_button1 = Button(description='resource diffusion coefficient', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='resource decay rate', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='quorum diffusion coefficient', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='quorum decay rate', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='death signal diffusion coefficient', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='death signal decay rate', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='attack signal diffusion coefficient', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='attack signal decay rate', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='poison diffusion coefficient', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='poison decay rate', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='number of randomly placed invaders', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='number of randomly placed suppliers', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='number of randomly placed scouts', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='number of randomly placed attackers', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='max birth rate for invaders', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='max death rate for invaders', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='persistence time for invader migration', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='speed of invader cells', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='invader migration bias', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='rate invaders secrete their signals', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='motile direction = w*grad(Q) - (1-w)*grad(D)', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='persistence time for scout migration', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='speed of scout cells', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='scout migration bias', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='rate scouts secrete their signals', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='scouts release S if Q > threshold', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='max birth rate for attackers', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='max death rate for attackers', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='persistence time for attacker migration', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='speed of attacker cells', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='attacker migration bias', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='rate attackers secrete their signals', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='attackers release P if S > threshold', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'
        desc_button34 = Button(description='rate suppliers release resource', disabled=True, layout=desc_button_layout) 
        desc_button34.style.button_color = 'tan'

        row1 = [param_name1, self.resource_D, units_button1, desc_button1] 
        row2 = [param_name2, self.resource_lambda, units_button2, desc_button2] 
        row3 = [param_name3, self.quorum_D, units_button3, desc_button3] 
        row4 = [param_name4, self.quorum_lambda, units_button4, desc_button4] 
        row5 = [param_name5, self.death_signal_D, units_button5, desc_button5] 
        row6 = [param_name6, self.death_signal_lambda, units_button6, desc_button6] 
        row7 = [param_name7, self.signal_D, units_button7, desc_button7] 
        row8 = [param_name8, self.signal_lambda, units_button8, desc_button8] 
        row9 = [param_name9, self.poison_D, units_button9, desc_button9] 
        row10 = [param_name10, self.poison_lambda, units_button10, desc_button10] 
        row11 = [param_name11, self.number_of_invaders, units_button11, desc_button11] 
        row12 = [param_name12, self.number_of_suppliers, units_button12, desc_button12] 
        row13 = [param_name13, self.number_of_scouts, units_button13, desc_button13] 
        row14 = [param_name14, self.number_of_attackers, units_button14, desc_button14] 
        row15 = [param_name15, self.invader_max_birth_rate, units_button15, desc_button15] 
        row16 = [param_name16, self.invader_max_death_rate, units_button16, desc_button16] 
        row17 = [param_name17, self.invader_persistence_time, units_button17, desc_button17] 
        row18 = [param_name18, self.invader_migration_speed, units_button18, desc_button18] 
        row19 = [param_name19, self.invader_migration_bias, units_button19, desc_button19] 
        row20 = [param_name20, self.invader_secretion_rate, units_button20, desc_button20] 
        row21 = [param_name21, self.invader_quorum_weight, units_button21, desc_button21] 
        row22 = [param_name22, self.scout_persistence_time, units_button22, desc_button22] 
        row23 = [param_name23, self.scout_migration_speed, units_button23, desc_button23] 
        row24 = [param_name24, self.scout_migration_bias, units_button24, desc_button24] 
        row25 = [param_name25, self.scout_secretion_rate, units_button25, desc_button25] 
        row26 = [param_name26, self.scout_signal_threshold, units_button26, desc_button26] 
        row27 = [param_name27, self.attacker_max_birth_rate, units_button27, desc_button27] 
        row28 = [param_name28, self.attacker_max_death_rate, units_button28, desc_button28] 
        row29 = [param_name29, self.attacker_persistence_time, units_button29, desc_button29] 
        row30 = [param_name30, self.attacker_migration_speed, units_button30, desc_button30] 
        row31 = [param_name31, self.attacker_migration_bias, units_button31, desc_button31] 
        row32 = [param_name32, self.attacker_secretion_rate, units_button32, desc_button32] 
        row33 = [param_name33, self.attacker_signal_threshold, units_button33, desc_button33] 
        row34 = [param_name34, self.supplier_secretion_rate, units_button34, desc_button34] 

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
