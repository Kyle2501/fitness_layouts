#!/usr/bin/python
# coding: latin-1

Site = 'Shanny Cohen Fitness'

Timezone = 'US/Mountain'

Colors = '''
    base03:    #002b36;
    base02:    #073642;
    base01:    #586e75;
    base00:    #657b83;
     base0:    #839496;
     base1:    #93a1a1;
     base2:    #eee8d5;
     base3:    #fdf6e3;
    yellow:    #b58900;
    orange:    #cb4b16;
       red:    #dc322f;
   magenta:    #d33682;
    violet:    #6c71c4;
      blue:    #268bd2;
      cyan:    #2aa198;
     green:    #859900;
''' # - http://ethanschoonover.com/solarized

Analytics = '''<script>

</script>'''

# - HTML Page Code



page_header = '''

'''

login_page_html = '''
  <div class="main_wrap-[!layout_style!]">
    <p>Sign in with your Google account</p>
  </div><!-- .main_wrap -->
'''


#----------------------------------------------#
#           Contact  page                      #
#----------------------------------------------#

#----------------------------------------------#
#           Exersice Publish Manage            #
#----------------------------------------------#

#----------------------------------------------#
#    Programs Signup and Payment               #
#----------------------------------------------#
silver_brozen_coupon_limit = 10


#----------------------------------------------#
#             Client Publish Manage            #
#----------------------------------------------#
#----------------------------------------------#
#             Waitlist Publish Manage          #
#----------------------------------------------#
manage_waitlist_page_html = '''
  <style type="text/css">
    .client_data { border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin: 15px auto 0 auto; }
  </style>
  <div class="main_wrap-[!layout_style!]">
    <a href='/publish/waitlist'><button>Add A New Client to Waitlist</button></a>
    <hr>
    <div class="input-group">
      <span>Seach:</span>
      <input ng-model='select_client' type="text">
      <p>
        Sort by: 
        <select  ng-model="sortBy" ng-init="sortBy = 'client_name' ">
            <option value="client_name" ng-selected>Client Name(&#8593;)</option>
            <option value="-client_name">Client Name(&#8595;)</option>
            <option value="client_email">Client Email(&#8593;)</option>
            <option value="-client_email">Client Email(&#8595;)</option>
            <option value="add_time">Add Time(&#8593;)</option>
            <option value="-add_time">Add Time(&#8595;)</option>
        </select>
      </p>
    </div><!-- .input-group -->

    <div class="client_data" ng-repeat="item in waitlist_data | orderBy: sortBy | filter:select_client">
        <p> Add Time:  [! item.add_time | limitTo: 19 !] </p>
        <p> Client Name:  [! item.client_name !] </p>  
        <p> Client Email:  [! item.client_email !] </p> 
        <p> Client Program:  [! item.client_program !] </p> 
        <p> Client Phone:  [! item.client_phone !] </p> 
        <p> Client Address:  [! item.client_address !] </p> 
        <a ng-href='/edit/waitlist?[!item.client_email!]'><button>Edit Info</button></a>
        <button ng-click="delete(item.client_email)">Remove</button>
    </div><!-- . exercise_data -->
  </div><!-- .main_wrap -->
'''
edit_waitlist_page_html = '''
  <style>
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap-[!layout_style!]">
    <header class="hi"><span class="color_b">Edit a Client in Waitlist</span></header>
   <article class="form_wrap">
      <form action="/manage/add_waitlist" method="post">
        <table>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" ng-model="item.client_name" required/></td>
          </tr>
          <tr>
            <td class="label">Program*</td>
            <td class="input">
              <select name="client_program" ng-model="item.client_program" required>
                <option ng-repeat="program in programs" value="[!program.name!]">[!program.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Email*</td>
            <td class="input"><input type="email" name="client_email" ng-model="item.client_email" required/></td>
          </tr>
          <tr>
            <td class="label">Client Phone</td>
            <td class="input"><input type="text" name="client_phone" ng-model="item.client_phone" /></td>
          </tr>
          <tr>
            <td class="label">Client Address</td>
            <td class="input"><input type="text" name="client_address" ng-model="item.client_address" /></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/waitlist"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - -->
''' 
publish_waitlist_page_html = '''
  <style>
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap-[!layout_style!]">
   <header class="hi"><span class="color_b">Add New Client to Waitlist</span></header>
   <article class="form_wrap">
      <form action="/manage/add_waitlist" method="post">
        <table>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" required/></td>
          </tr>
          <tr>
            <td class="label">Program*</td>
            <td class="input">
              <select name="client_program" required>
                <option ng-repeat="program in programs" value="[!program.name!]">[!program.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Email*</td>
            <td class="input"><input type="email" name="client_email" required/></td>
          </tr>
          <tr>
            <td class="label">Client Phone</td>
            <td class="input"><input type="text" name="client_phone" /></td>
          </tr>
          <tr>
            <td class="label">Client Address</td>
            <td class="input"><input type="text" name="client_address" /></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/waitlist"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - --> 
'''
#----------------------------------------------#
#            Client Workouts Manage            #
#----------------------------------------------#
manage_workout_page_html = '''
  <style type="text/css">
    .workout_data{border: 1px solid grey; text-align: left; padding: 10px; margin: 15px auto 0 auto;}
  </style>
 <div class="main_wrap-[!layout_style!]">
    <a href='/publish/[!client_group!]_workout'><button>Add A New Workout Plan</button></a>
    <hr>
    <div class="input-group">
      <span>Show data for client: </span>
      <select ng-model='select_client'>
        <option value="">All</option>
        <option ng-repeat="client_email in client_emails | orderBy: client_email" value="[!client_email!]">[!client_email!]</option>
      </select>
    </div>

    <div class="workout_data" ng-repeat="item in workout_data | orderBy: '-add_time' | filter:select_client">
        <p> For Client:  [! item.client_email !] </p>
        <p> Template:  [! item.template_name!] </p>
        <p> Add Time:  [! item.add_time!] </p>
        <a ng-href='/manage/view_[!client_group!]_workout?[!item.data_id!]'><button>View Workout Plan</button></a>
        <a ng-href='/edit/[!client_group!]_workout?[!item.data_id!]'><button>Edit Workout Plan</button></a>
        <button ng-click="delete(item.data_id)">Remove</button>
    </div><!--.workout_data-->
  </div><!-- .main_wrap -->
'''
manage_view_workout_page_html = '''
  <style type="text/css">
    .main_wrap a{text-decoration:underline;}
    .outter_wrap{width: 100%; overflow-x:scroll;}
    #workout_plan{width: 1200px; table-layout: fixed; }
    #workout_plan th{background:#37474F; color: #fff; padding: 5px; min-width: 100px;}
    #workout_plan td{padding: 5px; min-width: 100px;}
    .White, .Red, .Orange, .LightBlue, .LightGreen, .LightGrey, .BlueGrey {border:1px solid grey; padding: 10px 10px; margin: 5px auto;}
    .White{background:#fff;}
    .Red{background:#FFCDD2;}
    .Orange{background:#FFE0B2;}
    .LightBlue{background:#81D4FA;}
    .LightGreen{background:#B2DFDB;}
    .LightGrey{background:#E0E0E0;}
    .BlueGrey{background:#B0BEC5;}
    pre{ white-space: pre-wrap; white-space: -moz-pre-wrap; white-space: -pre-wrap;  white-space: -o-pre-wrap; word-wrap: break-word;}
  </style>
  <div class="main_wrap-[!layout_style!]">
    <header class="hi color_b">Exercise Plan for [!item.client_email!]</header>
    <a ng-href='/manage/[!client_group!]_workout'><button>Back</button></a>
    <a ng-href='/edit/[!client_group!]_workout?[!item.data_id!]'><button>Edit Workouts</button></a>
    <button ng-click="delete(item.data_id)">Remove Workouts</button>

    <p id="print_line1">[!item.program_date!]&nbsp;&nbsp;[!item.muscles!]&nbsp;&nbsp;[!item.client_email!]</p>
    <p id="print_line2">[!item.general_explanation!]</p>

    <div class="outter_wrap">
    <table id="workout_plan">

    <tr>
      <th>Exercise</th>
      <th>2 Warm up sets</th>
      <th>Set 1</th>
      <th>Set 2</th>
      <th>Set 3</th>
      <th class="set4" ng-show="table_length>=4">Set 4</th>
      <th class="set5" ng-show="table_length>=5">Set 5</th>
      <th>Image</th>
    </tr>

    <tr ng-repeat="exercise in item.workout" ng-class="exercise.exercise_color">
          <td><a href="/exercise_detail/?data_id=[!exercise.exercise_id!]" target="_blank">[!exercise.name!]</a><br>[!exercise.notes!]</td>
          <td><pre>[!exercise.warmup_set!]</pre></td>
          <td><pre>[!exercise.set1!]</pre></td>
          <td><pre>[!exercise.set2!]</pre></td>
          <td><pre>[!exercise.set3!]</pre></td>
          <td class="set4" ng-show="table_length>=4"><pre>[!exercise.set4!]</pre></td>
          <td class="set5" ng-show="table_length>=5"><pre>[!exercise.set5!]</pre></td>
          <td><img style="width:100px;" ng-src="/render_img?exercise?thumb?[!exercise.exercise_id!]"></pre></td>
    </tr><!-- .exercise_list -->
    </table>
    </div><!-- .outter_wrap -->

    <button ng-click="print_workout()">Print</button>
    <p>For Firefox and IE users to print the background color, please check the “Print Background Colors” on the Print dialog that is popped up.</p>
  </div><!-- .main_wrap -->
'''
edit_workout_page_html = '''
  <style>
  .form_wrap { width: 90%; margin: auto; }
  .small_form_wrap{padding:0; border: 1px solid #ccc;}
  tr { height: 32px; overflow-x:auto;}
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td.input { font-size: 14px; text-align: left; padding-left: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  .modal{ position: absolute; top: 0; z-index: 200;  padding: 25px; background: #fff; text-align: center; margin:auto;}
  .modal-backdrop{position: fixed; top: 0; left: 0; bottom: 0; right: 0;  z-index: 100;  background:rgba(0,0,0, 0.6);}
  .main_wrap a{text-decoration:underline;}
  .outter_wrap{width: 100%; overflow-x:scroll;}
  .workout_plan{width: 1200px; table-layout: fixed; }
  .workout_plan th{background:#37474F; color: #fff; padding: 5px; min-width: 100px;}
  .workout_plan td{padding: 5px; min-width: 100px;}
  .White, .Red, .Orange, .LightBlue, .LightGreen, .LightGrey, .BlueGrey {border:1px solid grey; padding: 10px 10px; margin: 5px auto;}
  .White{background:#fff;}
  .Red{background:#FFCDD2;}
  .Orange{background:#FFE0B2;}
  .LightBlue{background:#81D4FA;}
  .LightGreen{background:#B2DFDB;}
  .LightGrey{background:#E0E0E0;}
  .BlueGrey{background:#B0BEC5;}
  .btn_wrap{margin: 25px auto;}
  pre{ white-space: pre-wrap; white-space: -moz-pre-wrap; white-space: -pre-wrap;  white-space: -o-pre-wrap; word-wrap: break-word;}
  </style>

  <div class="main_wrap-[!layout_style!]">
   <header ng-show="!if_edit" class="hi"><span class="color_b">Add a Workout</span></header>
   <header ng-show="if_edit" class="hi"><span class="color_b">Edit Workout for [!item.client_email!]</span></header>

    <article class="form_wrap">
      <span >Use Template
        <select ng-model='template_id' name="template_name">
          <option ng-repeat="template in template_array | orderBy: this[0]" value="[!template[1]!]">[!template[0]!]</option>
        </select>
      </span>
      <button ng-click="set_workout_template()">Set</button>
      <hr>  

      <form ng-submit="save_workout_plan()" method="post">
        <table> 
          <tr class="hide">
            <td class="label">Data ID</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' ng-required="if_edit"></td>
          </tr>
          <tr class="hide">
            <td class="label">Template Name</td>
            <td class="input"><input type="text" name="template_name" ng-model='item.template_name' ></td>
          </tr>
          <tr>
            <td class="label">Client Email</td>
            <td class="input">
              <select name="client_email" ng-model='item.client_email' ng-options="client_email for client_email in client_emails | orderBy: client_email" required>
                <option value=""></option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Date</td>
            <td class="input"><input type="text" name="program_date" ng-model='item.program_date' placeholder="e.g. March 7-14" required/></td>
          </tr>
          <tr>
            <td class="label">Muscles</td>
            <td class="input"><input type="text" name="muscles" ng-model='item.muscles' placeholder="e.g. Quads/Calves" /></td>
          </tr>
          <tr>
            <td class="label">General Explanation</td>
            <td class="input"><textarea rows="3" cols="30" name="general_explanation" ng-model='item.general_explanation' placeholder="e.g. Super Sets with 90 second- 2 min Rest Between"> </textarea></td>
          </tr>
        </table>

        <div class="outter_wrap">
          <table class="workout_plan">

          <tr>
            <th>Index</th>
            <th>Exercise</th>
            <th>2 Warm up sets</th>
            <th>Set 1</th>
            <th>Set 2</th>
            <th>Set 3</th>
            <th>Set 4</th>
            <th>Set 5</th>
            <th>Image</th>
            <th>Delete</th>
            <th>Edit</th>
          </tr>

          <tr ng-repeat="exercise in item.workout" ng-class="exercise.exercise_color">
              <td><pre>[!$index+1!]</pre></td>
              <td>
                <a href="/exercise_detail/?data_id=[!exercise.exercise_id!]" target="_blank">[!exercise.name!]</a>
                <br>[!exercise.notes!]
              </td>
              <td><pre>[!exercise.warmup_set!]</pre></td>
              <td><pre>[!exercise.set1!]</pre></td>
              <td><pre>[!exercise.set2!]</pre></td>
              <td><pre>[!exercise.set3!]</pre></td>
              <td><pre>[!exercise.set4!]</pre></td>
              <td><pre>[!exercise.set5!]</pre></td>
              <td><img style="width:100px;" ng-src="/render_img?exercise?thumb?[!exercise.exercise_id!]"></td>
              <td><button type="button" ng-click="del_workout($index)">X</button></td>
              <td><button type="button" ng-click="edit_workout($index)">Edit</button></td>
          </tr><!-- .exercise_list -->
          </table>
        </div><!-- .outter_wrap -->

        <div class="btn_wrap">
          <button type="button" ng-click="new_workout()">Add an Exercise</button>
          <button type="button" ng-click="if_insert = true;new_workout()">Insert an Exercise</button>
        </div><!-- - .btn_wrap - -->

        <div class="btn_wrap">
          <a href="/manage/[!client_group!]_workout"><button type="button">Cancel</button></a>
          <input type="submit" value="Save">
        </div><!-- - .btn_wrap - -->
      </form>
    </article><!-- - /form_wrap - -->

    <div class="modal" ng-show="if_modal_show">
      <article class="small_form_wrap">
        <form  method="post" ng-submit="add_workout()">
         <table>
          <tr>
            <td class="label">Exercise Name</td>
            <td class="input">
              <input type="text" placeholder="e.g. Push Ups" ng-model='select_name'>
            </td>
          </tr>
          <tr>
            <td class="label"></td>
            <td class="input">
              <select ng-model='tmp.exercise_id' name="exercise_name" required>
                <option ng-repeat="exercise in exercise_array | filter: select_name | orderBy: this[0]" value="[!exercise[1]!]">[!exercise[0]!]</option>
              </select>
            </td>
          </tr>
          <tr ng-show="if_insert">
            <td class="label">Insert Index</td>
            <td class="input">
              <select ng-model='tmp.exercise_idx' name="exercise_idx" required>
                <option ng-repeat="$index in item.workout | orderBy: $index" value="[!$index!]">[!$index+1!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Exercise Color</td>
            <td class="input">
              <select ng-model='tmp.exercise_color' name="exercise_color">
                <option ng-repeat="color in color_list" value="[!color!]">[!color!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Notes</td>
            <td class="input"><textarea rows="3" cols="30" name="notes" ng-model='tmp.notes' placeholder="e.g. 2*SUPERSET (Weight in heel)"></textarea></td>
          </tr>
          <tr>
            <td class="label">Warm up set</td>
            <td class="input"><textarea rows="3" cols="30" name="warmup_set" ng-model='tmp.warmup_set'></textarea></td>
          </tr>
          <tr>
            <td class="label">Set 1</td>
            <td class="input"><textarea rows="3" cols="30" name="set1" ng-model='tmp.set1' ></textarea></td>
          </tr>
          <tr>
            <td class="label">Set 2</td>
            <td class="input"><textarea rows="3" cols="30" name="set2" ng-model='tmp.set2' ></textarea></td>
          </tr>
          <tr>
            <td class="label">Set 3</td>
            <td class="input"><textarea rows="3" cols="30" name="set3" ng-model='tmp.set3' ></textarea></td>
          </tr>
          <tr>
            <td class="label">Set 4</td>
            <td class="input"><textarea rows="3" cols="30" name="set4" ng-model='tmp.set4' ></textarea></td>
          </tr>
          <tr>
            <td class="label">Set 5</td>
            <td class="input"><textarea rows="3" cols="30" name="set5" ng-model='tmp.set5' ></textarea></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <button type="button" ng-click="if_modal_show=flase;if_insert=false;">Cancel</button>
              <input type="submit" value="Add" />
            </td>
          </tr>
        </table>
        </form>
      </article><!-- - .small_form_wrap - -->
      <button type="button" ng-click="if_modal_show=flase;if_insert=false;">Close</button>
    </div><!--.modal-->

    <div class="modal-backdrop" ng-show="if_modal_show"></div>

  </div><!-- - .main_wrap - -->
'''
#----------------------------------------------#
#           Workouts Template Manage           #
#----------------------------------------------#
manage_template_page_html = '''
  <style type="text/css">
    .template_data { border: 1px solid grey; text-align: left; padding: 10px; margin: 15px auto 0 auto; }
  </style>
 <div class="main_wrap-[!layout_style!]">
    <a href='/publish/template'><button>Add A New Template</button></a>
    <hr>
    <div class="input-group">
      <span>Seach:</span>
      <input ng-model='select_template' type="text">
    </div>

    <div class="template_data" ng-repeat="item in template_data | orderBy: '-add_time' | filter:select_template">
        <p> Template Name: <strong> [! item.template_name !] </strong></p> 
        <p> Author:  [! item.author !] </p>  
        <p> Add Time:  [! item.add_time|limitTo:4 !]-[! item.add_time|limitTo:2:4 !]-[! item.add_time|limitTo:2:6 !] </p>
        <a ng-href='/manage/view_template?[!item.data_id!]'><button>View Template</button></a>
        <a ng-href='/edit/template?[!item.data_id!]'><button>Edit Template</button></a>
        <button ng-click="delete(item.data_id)">Remove</button>
    </div><!-- . exercise_data -->
  </div><!-- . main_wrap -->
'''
manage_view_template_page_html_old = '''
  <style type="text/css">
    .main_wrap a { text-decoration: underline; }
    .outter_wrap { width: 100%; overflow-x: scroll; }
    .workout_plan { width: 1200px; table-layout: fixed; }
    .workout_plan th { background:#37474F; color: #fff; padding: 5px; min-width: 100px; }
    .workout_plan td { padding: 5px; min-width: 100px; }
    .White, .Red, .Orange, .LightBlue, .LightGreen, .LightGrey, .BlueGrey {border:1px solid grey; padding: 10px 10px; margin: 5px auto; }
    .White { background: #fff; }
    .Red { background: #FFCDD2; }
    .Orange { background:#FFE0B2;}
    .LightBlue { background:#81D4FA; }
    .LightGreen { background:#B2DFDB; }
    .LightGrey { background:#E0E0E0; }
    .BlueGrey { background:#B0BEC5; }
    pre{ white-space: pre-wrap; white-space: -moz-pre-wrap; white-space: -pre-wrap;  white-space: -o-pre-wrap; word-wrap: break-word; }
    .hi { color: #fff; }
  </style>
  <div class="main_wrap-[!layout_style!]">
     <header class="hi">Template [!item.template_name!]</header>
      <a ng-href='/manage/template'><button>Back</button></a>
      <a ng-href='/edit/template?[!item.data_id!]'><button>Edit Template</button></a>
      <button ng-click="delete(item.data_id)">Remove</button>

        <p>[!item.program_date!]&nbsp;&nbsp;[!item.muscles!]&nbsp;&nbsp;[!item.client_name!]</p>
        <p>[!item.general_explanation!]</p>

        <div class="outter_wrap">
        <table class="workout_plan">

        <tr>
          <th>Exercise</th>
          <th>Warm up sets</th>
          <th>Set 1</th>
          <th>Set 2</th>
          <th>Set 3</th>
          <th ng-show="table_length>=4">Set 4</th>
          <th ng-show="table_length>=5">Set 5</th>
          <th>Image</th>
        </tr>

        <tr ng-repeat="exercise in item.workout" ng-class="exercise.exercise_color">
              <td><a href="/exercise_detail/?data_id=[!exercise.exercise_id!]" target="_blank">[!exercise.name!]</a><br>[!exercise.notes!]</td>
              <td><pre>[!exercise.warmup_set!]</pre></td>
              <td><pre>[!exercise.set1!]</pre></td>
              <td><pre>[!exercise.set2!]</pre></td>
              <td><pre>[!exercise.set3!]</pre></td>
              <td ng-show="table_length>=4"><pre>[!exercise.set4!]</pre></td>
              <td ng-show="table_length>=5"><pre>[!exercise.set5!]</pre></td>
              <td><img style="width:100px;" ng-src="/render_img?exercise?thumb?[!exercise.exercise_id!]"></td>
        </tr><!-- .exercise_list -->
        </table>
        </div><!-- .outter_wrap -->

  </div><!-- .main_wrap -->
'''
#----------------------------------------------#
#             Client Interface                 #
#----------------------------------------------#


change_program_success_page_html ='''
  <div class="main_wrap-[!layout_style!]">
  <h2>You have successfully changed your program. </h2>
  <h2>You will be billed the amount for the new program in the next bill.</h2>
  </div><!-- .main_wrap -->
'''
change_credit_card_success_page_html ='''
  <div class="main_wrap-[!layout_style!]">
  <h2>Your have successfully change your credit card.</h2>
  </div><!-- .main_wrap -->
'''
#----------------------------------------------#
#             Code                             #
#----------------------------------------------#
import os
import urllib
import wsgiref.handlers
import webapp2
from webapp2_extras import routes
import json
import logging
# - 
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
# -
from google.appengine.ext import db
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
# -
from urlparse import urlparse
import urllib2
# -
import time
import datetime
from pytz.gae import pytz
#- stripe
import stripe
stripe.api_key = "sk_live_BohSO0M0PuJiFAJWGTztzzJd"

import fitness_page_code as html
import scfit_public_page_code as public_html
import scfit_account_page_code as account_html
import scfit_manage_page_code as manage_html
import scfit_workout_html as workout_html





#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class BikiniBootcamp_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()

    @classmethod
    def _get_all_data(self):
        q = ndb.gql('SELECT data_id, add_time, user_name, video_id, video_name, video_text, video_key FROM BikiniBootcamp_db')
        db_data = []
        for item in q.iter():
          db_data.append({'data_id': item.data_id, 'add_time': str(item.add_time), 'user_name': item.user_name, 'video_id': item.video_id, 'video_name': item.video_name, 'video_text': item.video_text, 'video_key': item.video_key})
        return json.dumps(db_data)

    @classmethod
    def _get_one_data(self,data_id):
        # item = Exercise_db.get_by_id(data_id)
        q =ndb.gql('SELECT user_name, video_id, video_name, video_text, video_key FROM BikiniBootcamp_db WHERE data_id= :1', data_id)

        db_data={}
        for item in q:
          db_data = {'data_id': data_id, 'video_id': item.video_id, 'video_name': item.video_name, 'video_text': item.video_text}
        return json.dumps(db_data)

    @classmethod
    def _get_all_names(self):
        q =ndb.gql('SELECT data_id, exercise_name from BikiniBootcamp_db')
        db_data = {}
        for item in q.iter():
          db_data[item.data_id] = item.exercise_name
        return json.dumps(db_data)

class addBikiniBootcamp_db(webapp2.RequestHandler):
  def post(self):

    if users.is_current_user_admin():
      data_id = self.request.get('data_id')
      if data_id and data_id != '':
        item = BikiniBootcamp_db.get_by_id(data_id)
      else:
        data_id = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d%H%M%S")
        item = BikiniBootcamp_db(id=data_id)
        item.data_id = data_id
      # - -
      item.user_name = users.get_current_user().nickname()
      item.video_id = data_id
      item.video_name = self.request.get('video_name')
      item.video_text = self.request.get('video_text')

      
      video_icon = self.request.get('image_file')
      if video_icon:
        item.video_icon = images.resize(video_icon, 800, 600)
      #
      item.put()
      time.sleep(1)
      self.redirect('/publish/bikini_bootcamp_upload?{0}'.format(data_id))

class UploadBikiniBootcampVideo(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        try:
            upload = self.get_uploads()[0]
            data_id = self.request.get('data_id')
            item = BikiniBootcamp_db.get_by_id(data_id)

            if item:
              if item.video_key and len(item.video_key) > 0:
                blobkey = blobstore.blobstore.BlobKey(item.video_key)
                blobstore.delete(blobkey)
                item.video_key = str(upload.key())
              else:
                item.video_key = str(upload.key())
              item.put()
              self.redirect('/manage/bikini_bootcamp')
        except:
            self.error(500)










#----------------------------------------------#
#           Homepage Data Stucture             #
#----------------------------------------------#
class Homepage_video_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_photo = ndb.BlobProperty()
    video_key = ndb.StringProperty()

    @classmethod
    def _get_all_data(self):
        q = ndb.gql('SELECT data_id, add_time, user_name, video_id, video_name, video_text, video_key FROM Homepage_video_db')
        db_data = []
        for item in q.iter():
          db_data.append({'data_id': item.data_id, 'add_time': str(item.add_time), 'user_name': item.user_name, 'video_id': item.video_id, 'video_name': item.video_name, 'video_text': item.video_text, 'video_key': item.video_key})
        return json.dumps(db_data)

    @classmethod
    def _get_one_data(self,data_id):
        # item = Exercise_db.get_by_id(data_id)
        q =ndb.gql('SELECT user_name, video_id, video_name, video_text, video_key FROM Homepage_video_db WHERE data_id= :1', data_id)

        db_data={}
        for item in q:
          db_data = {'data_id': data_id, 'video_id': item.video_id, 'video_name': item.video_name, 'video_text': item.video_text}
        return json.dumps(db_data)

    @classmethod
    def _get_all_names(self):
        q =ndb.gql('SELECT data_id, exercise_name from Homepage_video_db')
        db_data = {}
        for item in q.iter():
          db_data[item.data_id] = item.exercise_name
        return json.dumps(db_data)

class addHomepage_video_db(webapp2.RequestHandler):
  def post(self):

    if users.is_current_user_admin():
      data_id = self.request.get('data_id')
      if data_id and data_id != '':
        item = Homepage_video_db.get_by_id(data_id)
      else:
        data_id = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d%H%M%S")
        item = Homepage_video_db(id=data_id)
        item.data_id = data_id
      # - -
      item.user_name = users.get_current_user().nickname()
      item.video_id = data_id
      item.video_name = self.request.get('video_name')
      item.video_text = self.request.get('video_text')

      
      video_photo = self.request.get('video_photo')
      if video_photo:
        item.video_photo = images.resize(exercise_photo, 800, 600)
      #
      item.put()
      time.sleep(1)
      self.redirect('/publish/homepage_video_upload?{0}'.format(data_id))

class UploadHomepageVideo(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        try:
            upload = self.get_uploads()[0]
            data_id = self.request.get('data_id')
            item = Homepage_video_db.get_by_id(data_id)

            if item:
              if item.video_key and len(item.video_key) > 0:
                blobkey = blobstore.blobstore.BlobKey(item.video_key)
                blobstore.delete(blobkey)
                item.video_key = str(upload.key())
              else:
                item.video_key = str(upload.key())
              item.put()
              self.redirect('/manage/homepage_video')
        except:
            self.error(500)



#----------------------------------------------#
#           Exercise Data Stucture             #
#----------------------------------------------#
class Exercise_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
    #
    user_name = ndb.StringProperty()
    #
    exercise_id = ndb.StringProperty()
    exercise_name = ndb.StringProperty()
    difficulty_level = ndb.StringProperty()
    equipment_type = ndb.StringProperty()
    # muscle_targeted = ndb.StringProperty(repeated=True)
    muscle_targeted = ndb.StringProperty()
    exercise_photo = ndb.BlobProperty()
    exercise_video_key = ndb.StringProperty()

    @classmethod
    def _get_all_data(self):
        q = ndb.gql('SELECT data_id, add_time, user_name, exercise_name, difficulty_level, equipment_type, muscle_targeted, exercise_video_key FROM Exercise_db')
        db_data = []
        for item in q.iter():
          db_data.append({'data_id': item.data_id, 'add_time': str(item.add_time), 'user_name': item.user_name, 'exercise_name': item.exercise_name, 'difficulty_level': item.difficulty_level, 'equipment_type': item.equipment_type, 'muscle_targeted': item.muscle_targeted, 'exercise_video_key': item.exercise_video_key})
        return json.dumps(db_data)

    @classmethod
    def _get_one_data(self,data_id):
        # item = Exercise_db.get_by_id(data_id)
        q =ndb.gql('SELECT exercise_name, difficulty_level, equipment_type, muscle_targeted, exercise_video_key from Exercise_db WHERE data_id= :1', data_id)

        db_data={}
        for item in q:
          db_data = {'data_id': data_id, 'exercise_name': item.exercise_name,'difficulty_level': item.difficulty_level, 'equipment_type': item.equipment_type, 'muscle_targeted': item.muscle_targeted, 'exercise_video_key': item.exercise_video_key}
        return json.dumps(db_data)

    @classmethod
    def _get_all_names(self):
        q =ndb.gql('SELECT data_id, exercise_name from Exercise_db')
        db_data = {}
        for item in q.iter():
          db_data[item.data_id] = item.exercise_name
        return json.dumps(db_data)

class addExercise_db(webapp2.RequestHandler):
  def post(self):

    if users.is_current_user_admin():
      data_id = self.request.get('data_id')
      if data_id and data_id != '':
        item = Exercise_db.get_by_id(data_id)
      else:
        data_id = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d%H%M%S")
        item = Exercise_db(id=data_id)
        item.data_id = data_id
      # - -
      item.user_name = users.get_current_user().nickname()
      item.exercise_id = self.request.get('exercise_id')
      item.exercise_name = self.request.get('exercise_name')
      item.difficulty_level = self.request.get('difficulty_level')
      item.equipment_type = self.request.get('equipment_type')
      muscle_targeted = self.request.POST.getall('muscle_targeted')
      item.muscle_targeted = ', '.join(muscle_targeted)
      
      exercise_photo = self.request.get('exercise_photo')
      if exercise_photo:
        item.exercise_photo = images.resize(exercise_photo, 800, 600)
      #
      item.put()
      time.sleep(1)
      self.redirect('/manage/exercise')

class reset_exe_db(webapp2.RequestHandler):
  def get(self):
    q = Exercise_db.query()
    for item in q.iter():
      item.difficulty_level = 'Beginner'
      item.put()
      time.sleep(1)






#----------------------------------------------#
#      Template Data Stucture                  #
#----------------------------------------------#
class Template_db(ndb.Model):
  data_id = ndb.StringProperty()
  add_time = ndb.StringProperty()
  author = ndb.StringProperty()
  template_name = ndb.StringProperty()
  muscles = ndb.StringProperty()
  general_explanation = ndb.StringProperty()

  workout = ndb.JsonProperty()

  @classmethod
  def _get_one_data(self,data_id):
      item = Template_db.get_by_id(data_id)
      if item:
        db_data = item.to_dict()
      else: 
        db_data = None
      return json.dumps(db_data)

  @classmethod
  def _get_all_data(self):
      q = ndb.gql('SELECT data_id, add_time, author, template_name from Template_db') 
      db_data = []
      for item in q.iter():
        db_data.append(item.to_dict())
      return json.dumps(db_data)

  @classmethod
  def _get_all_names(self):
      q = ndb.gql('SELECT data_id, template_name from Template_db') 
      db_data = {}
      for item in q.iter():
        db_data[item.data_id] = item.template_name
      return json.dumps(db_data)

class addTemplate_db(webapp2.RequestHandler):
  def post(self):
    if users.is_current_user_admin():
      request_data = json.loads(self.request.body)
      data_id = request_data.get('data_id')

      if data_id and data_id != '':
        item = Template_db.get_by_id(data_id)
      else:
        data_id = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d%H%M%S")
        item = Template_db(id=data_id)
        item.data_id = data_id
        item.add_time = data_id
      # - -
      item.author = users.get_current_user().email()
      item.template_name = request_data.get('template_name')
      item.muscles = request_data.get('muscles_array')
      item.general_explanation = request_data.get('general_explanation')
      item.workout = request_data.get('workout')
      
      item.put()
      time.sleep(1)

#----------------------------------------------#
#      Workout Data Stucture                   #
#----------------------------------------------#
class Workout_db(ndb.Model):
  add_time = ndb.StringProperty()
  data_id = ndb.StringProperty()
  template_name = ndb.StringProperty()
  program_date = ndb.StringProperty()
  muscles = ndb.StringProperty()
  client_email = ndb.StringProperty()
  general_explanation = ndb.StringProperty()

  workout = ndb.JsonProperty()

  @classmethod
  def _get_all_pg_data(self):
      q = ndb.gql('SELECT data_id, add_time, client_email, template_name from Workout_db') 
      db_data = []
      for item in q.iter():
        if item.client_email != 'silver_member' and item.client_email != 'bronze_member':
          db_data.append(item.to_dict())
      return json.dumps(db_data)

  @classmethod
  def _get_all_sb_data(self):
      q = ndb.gql('SELECT data_id, add_time, client_email, template_name from Workout_db') 
      db_data = []
      for item in q.iter():
        if item.client_email == 'silver_member' or item.client_email == 'bronze_member':
          db_data.append(item.to_dict())
      return json.dumps(db_data)

  @classmethod
  def _get_all_silver_data(self):
      q = ndb.gql('SELECT data_id, add_time, client_email, template_name from Workout_db') 
      db_data = []
      for item in q.iter():
        if item.client_email == 'silver_member':
          db_data.append(item.to_dict())
      return json.dumps(db_data)

  @classmethod
  def _get_all_bronze_data(self):
      q = ndb.gql('SELECT data_id, add_time, client_email, template_name from Workout_db') 
      db_data = []
      for item in q.iter():
        if item.client_email == 'bronze_member':
          db_data.append(item.to_dict())
      return json.dumps(db_data)

  @classmethod
  def _get_one_data(self,data_id):
      item = Workout_db.get_by_id(data_id)
      if item:
        db_data = item.to_dict()
      else: 
        db_data = None
      return json.dumps(db_data)

  @classmethod
  def _get_current_workout(self):
      client_email = users.get_current_user().email()
      q = Workout_db.query(Workout_db.client_email == client_email)
      db_data = []
      for item in q.iter():
        db_data.append(item.to_dict())
      return json.dumps(db_data)

  @classmethod
  def _del_client_workout(self, client_email):
      q = Workout_db.query(Workout_db.client_email == client_email)
      db_data = []
      for item in q.iter():
          item.key.delete()
          time.sleep(1)

class addWorkout_db(webapp2.RequestHandler):
  def post(self):
    if users.is_current_user_admin():
      request_data = json.loads(self.request.body)
      data_id = request_data.get('data_id')
      item = None

      if data_id and data_id != '':
        item = Workout_db.get_by_id(data_id)
         
      if not item:
        data_id = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d%H%M%S")
        item = Workout_db(id=data_id)
        item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y-%m-%d %H:%M:%S")
        item.data_id = data_id

      # - -
      item.program_date = request_data.get('program_date')
      item.muscles = request_data.get('muscles')
      item.template_name = request_data.get('template_name')
      item.client_email = request_data.get('client_email')
      item.general_explanation = request_data.get('general_explanation')
      item.workout = request_data.get('workout')

      if item.client_email == 'silver_member' or item.client_email == 'bronze_member':
        item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y-%m-%d %H:%M:%S")

      item.put()
      time.sleep(1)

#----------------------------------------------#
#      Client and Waitlist Data Stucture       #
#----------------------------------------------#
class Client_db(ndb.Model):
  add_time = ndb.StringProperty()
  #
  # client_id = ndb.StringProperty()
  client_name = ndb.StringProperty()
  client_program = ndb.StringProperty()
  program_status = ndb.StringProperty()
  stripe_cus_id = ndb.StringProperty()
  stripe_subscription_id = ndb.StringProperty()
  client_email = ndb.StringProperty()
  client_phone = ndb.StringProperty()
  client_address = ndb.TextProperty()

  
  has_photo = ndb.BooleanProperty()
  client_photo = ndb.BlobProperty()
#
  main_sport = ndb.StringProperty()

  @classmethod
  def _get_all_data(self):
      q = Client_db.query()
      db_data = []
      for item in q.iter():
        db_data.append(item.to_dict(exclude=['client_photo']))
      return json.dumps(db_data)

  @classmethod
  def _get_pg_emails(self):
    q = Client_db.query(ndb.OR(Client_db.client_program == 'Platinum',Client_db.client_program == 'Gold')).fetch(projection=[Client_db.client_email])
    db_data = []
    for item in q:
      db_data.append(item.client_email) 
    return json.dumps(db_data)

  @classmethod
  def _get_one_data(self,data_id):
      item = Client_db.get_by_id(data_id)
      if item:
        db_data = item.to_dict(exclude=['client_photo'])
      else: 
        db_data = []
      return json.dumps(db_data)

  @classmethod
  def _in_this_db(self,client_id):
      q = Client_db.get_by_id(client_id)
      if q:
        return True
      else:
        return False

  @classmethod
  def _count_client(self):
      q1 = Client_db.query( ndb.AND(Client_db.client_program == 'Platinum',Client_db.program_status == 'Active') ).fetch(keys_only = True)
      q2 = Client_db.query( ndb.AND(Client_db.client_program == 'Gold',Client_db.program_status == 'Active') ).fetch(keys_only = True)
      q3 = Client_db.query( ndb.AND(Client_db.client_program == 'Silver',Client_db.program_status == 'Active') ).fetch(keys_only = True)
      q4 = Client_db.query( ndb.AND(Client_db.client_program == 'Bronze',Client_db.program_status == 'Active') ).fetch(keys_only = True)
      return json.dumps({'Platinum':len(q1),'Gold':len(q2), 'Silver':len(q3), 'Bronze':len(q4)})
      # return json.dumps([len(q1), len(q2), len(q3), len(q4)])

  @classmethod
  def _get_current_client(self):
      client_email = users.get_current_user().email()
      item = Client_db.get_by_id(client_email)
      if item:
        db_data = item.to_dict(exclude=['client_photo'])
      else: 
        db_data = []
      return json.dumps(db_data)

class addClient_db(webapp2.RequestHandler):
  def post(self):

    if users.is_current_user_admin():

      client_email = self.request.get('client_email')

      if client_email and client_email != '':
        item = Client_db.get_by_id(client_email)
        if not item:
          item = Client_db(id=client_email)
          item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")

      # - -
      item.client_name = self.request.get('client_name')
      item.client_email = self.request.get('client_email')
      item.client_program = self.request.get('client_program')
      item.program_status = self.request.get('program_status')
      item.stripe_cus_id = self.request.get('stripe_cus_id')
      item.stripe_subscription_id = self.request.get('stripe_subscription_id')
      item.client_program = self.request.get('client_program')
      item.client_phone = self.request.get('client_phone')
      item.client_address = self.request.get('client_address')
      
      client_photo = self.request.get('client_photo')
      if client_photo:
        item.client_photo = images.resize(client_photo, 800, 600)
        item.has_photo = True
      else:
        if not item.client_photo:
          item.has_photo = False
      #
      item.put()
      time.sleep(1)
      self.redirect('/manage/client')

class addClient_db_user(webapp2.RequestHandler):
  def post(self):
    client_email = self.request.get('client_email')
    item = Client_db.get_by_id(client_email)

    if not item:
      item = Client_db(id=client_email)
      item.client_email = self.request.get('client_email')
      item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")

    item.client_name = self.request.get('client_name')
    item.client_phone = self.request.get('client_phone')
    item.client_address = self.request.get('client_address')
    
    client_photo = self.request.get('client_photo')
    if client_photo:
      item.client_photo = images.resize(client_photo, 800, 600)
      item.has_photo = True
    else:
      if not item.client_photo:
        item.has_photo = False
    #
    item.put()
    self.redirect('/my_account/my_info')

class Waitlist_db(ndb.Model):
  add_time = ndb.StringProperty()
  #
  client_name = ndb.StringProperty()
  client_program = ndb.StringProperty()
  client_email = ndb.StringProperty()
  client_phone = ndb.StringProperty()
  client_address = ndb.TextProperty()

  @classmethod
  def _get_all_data(self):
      q = Waitlist_db.query()
      db_data = []
      for item in q.iter():
        db_data.append(item.to_dict())
      return json.dumps(db_data)

  @classmethod
  def _get_one_data(self,data_id):
    item = Waitlist_db.get_by_id(data_id)
    if item:
      db_data = item.to_dict()
    else: 
      db_data = []
    return json.dumps(db_data)

  @classmethod
  def _get_current_waitlist(self):
      client_email = users.get_current_user().email()
      item = Waitlist_db.get_by_id(client_email)
      if item:
        db_data = item.to_dict()
      else: 
        db_data = []
      return json.dumps(db_data)

class addWaitlist_db(webapp2.RequestHandler):
  def post(self):

    if users.get_current_user():

      client_email = self.request.get('client_email')
      if client_email:
        item = Waitlist_db.get_by_id(client_email)
        if not item:
          item = Waitlist_db(id=client_email)
          item.client_email = self.request.get('client_email')
          item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")

        item.client_program = self.request.get('client_program')
        item.client_name = self.request.get('client_name')
        item.client_phone = self.request.get('client_phone')
        item.client_address = self.request.get('client_address')
        item.put()
        time.sleep(1)

        if users.is_current_user_admin():
          self.redirect('/manage/waitlist')
        else:
          self.redirect('/my_program')



#----------------------------------------------#
#           Testimonial Data Stucture          #
#----------------------------------------------#
class Testimonial_db(ndb.Model):
    add_time = ndb.StringProperty()
    data_id = ndb.StringProperty()
    client_name = ndb.StringProperty()
    client_email = ndb.StringProperty()
    testimonial_text = ndb.TextProperty()
    testimonial_photo = ndb.BlobProperty()
    has_photo = ndb.BooleanProperty()

    @classmethod
    def _get_all_data(self):
        q = Testimonial_db.query()
        db_data = []
        for item in q.iter():
          db_data.append(item.to_dict(exclude=['testimonial_photo']))
        return json.dumps(db_data)

    @classmethod
    def _get_one_data(self,data_id):
        item = Testimonial_db.get_by_id(data_id)
        if item:
          db_data = item.to_dict(exclude=['testimonial_photo'])
        else: 
          db_data = []
        return json.dumps(db_data)

    @classmethod
    def _get_current_testimonial(self):
        client_email = users.get_current_user().email()
        q = Testimonial_db.query(Testimonial_db.client_email == client_email)
        db_data = []
        for item in q.iter():
          db_data.append(item.to_dict(exclude=['testimonial_photo']))
        return json.dumps(db_data)

class addTestimonial_db(webapp2.RequestHandler):
    def post(self):

      user = users.get_current_user()

      if user:

        data_id = self.request.get('data_id')
        if data_id and data_id != '':
          item = Testimonial_db.get_by_id(data_id)
        else:
          data_id = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d%H%M%S")
          item = Testimonial_db(id=data_id)
          item.data_id = data_id
          item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")
          item.client_email = user.email()

        item.client_name = self.request.get('client_name')
        item.testimonial_text= self.request.get('testimonial_text')

        testimonial_photo = self.request.get('testimonial_photo')
        if testimonial_photo:
          item.testimonial_photo = images.resize(testimonial_photo, 800, 600)
          item.has_photo = True
        else:
          if not item.testimonial_photo:
            item.has_photo = False

        item.put()
        time.sleep(1)

        if users.is_current_user_admin():
          self.redirect('/manage/testimonial')
        else:
          self.redirect('/my_account/my_testimonial')



#----------------------------------------------#
#           Contact page                       #
#----------------------------------------------#
class verifyRecaptcha(webapp2.RequestHandler):
  def post(self):
    request_data = json.loads(self.request.body)
    user_response = request_data.get('g-recaptcha-response')

    data = {'secret': '6LcPLh4TAAAAALCfpJ9Z8s81gTc14mbolydjyaUC', 'response':user_response}
    url = 'https://www.google.com/recaptcha/api/siteverify'

    data = urllib.urlencode(data)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    response = response.read()

    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(response)    

class submitQuestion(webapp2.RequestHandler):
  def post(self):
    request_data = json.loads(self.request.body)

    client_name = request_data.get('client_name')
    client_email = request_data.get('client_email')
    client_address = request_data.get('client_address')
    client_question = request_data.get('client_question')
    submit_time = int(time.time())

    #--mail to host
    message = mail.EmailMessage(sender="Web Question <ShannyCohen.Fitness@gmail.com>", subject="Question Recieved #" + str(submit_time))   
    message.to = "ShannyCohen.Fitness@gmail.com"
    message.reply_to = str(client_email)
    message.body = "Name: " + str(client_name) + "\n\n Email: " + str(client_email) + "\n\n Address: " + str(client_address) + "\n\n Question: \n" + str(client_question)
    message.send()

    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write('200')   

    # self.redirect('/contact_success')


#----------------------------------------------#
#             Payment Records                  #
#----------------------------------------------#
class chargeCard(webapp2.RequestHandler):
  def post(self):
    # stripe.Plan.create(
    #   amount=55000,
    #   interval='month',
    #   name='Platinum',
    #   currency='usd',
    #   id='Platinum')

    # Get the credit card details submitted by the form
    token = self.request.POST['stripeToken']
    client_email = users.get_current_user().email()
    # data_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if not Client_db._in_this_db(client_email):
      item = Client_db(id=client_email)
    else:
      item = Client_db.get_by_id(client_email)
 
    item.client_name = self.request.get('client_name')
    item.client_email = self.request.get('client_email')
    item.client_program = self.request.get('client_program')
    item.client_phone = self.request.get('client_phone')
    item.client_address = self.request.get('client_address')
    if not item.client_photo:
      item.has_photo = False
    item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")
    
    # - create stripe customer
    try:
      # coupon for silver and brozen customers
      # if item.client_program == 'Silver' or item.client_program == 'Bronze':
      #   client_count = json.loads(Client_db._count_client())
      #   if client_count["Silver"] + client_count["Bronze"] < silver_brozen_coupon_limit:
      #     customer = stripe.Customer.create(
      #     source=token,
      #     plan=item.client_program,
      #     email=item.client_email,
      #     coupon="50%OFF"
      #     )
      #   else:
      #     customer = stripe.Customer.create(
      #     source=token,
      #     plan=item.client_program,
      #     email=item.client_email
      #     )
      # else:
        customer = stripe.Customer.create(
        source=token,
        plan=item.client_program,
        email=item.client_email
        )
    except stripe.error.CardError, e:
        self.response.out.write(str(e)) 
    except stripe.error.RateLimitError, e:
        self.response.out.write(str(e)) 
    except stripe.error.InvalidRequestError, e:
        self.response.out.write(str(e)) 
    except stripe.error.AuthenticationError, e:
        self.response.out.write(str(e)) 
    except stripe.error.APIConnectionError, e:
        self.response.out.write(str(e)) 
    except stripe.error.StripeError, e:
        self.response.out.write(str(e)) 
    else:
      item.program_status = 'Active'
      item.stripe_cus_id = customer["id"]
      item.stripe_subscription_id = customer["subscriptions"]["data"][0]["id"]
      item.put()

      #--mail to client
      message = mail.EmailMessage(sender="Shanny Cohen Fitness <ShannyCohen.Fitness@gmail.com>", subject="Confirmation of Program Enrollment")    
      message.to = item.client_email
      message.reply_to = "ShannyCohen.Fitness@gmail.com"
      message.body = "Dear " + str(item.client_name) + ", \n\n You have enrolled in the following program: " + "\n " + str(item.client_program) + '\n\n Shanny Cohen Personal Training LLC.'
      message.send()

      #--mail to shanny
      message2 = mail.EmailMessage(sender="Shanny Cohen Fitness <ShannyCohen.Fitness@gmail.com>", subject="New Client " + str(item.client_email))    
      message2.to = "ShannyCohen.Fitness@gmail.com"
      message2.body = "A new client " + str(item.client_name) + " has signed up for the " +  str(item.client_program) + ' Program.'
      message2.send()

      self.redirect('/payment_success')

class cancelProgram(webapp2.RequestHandler):
  def get(self):
    if users.get_current_user():
      client_email = users.get_current_user().email()
      item = Client_db.get_by_id(client_email)
      
      try:
        customer = stripe.Customer.retrieve(item.stripe_cus_id)
        customer.subscriptions.retrieve(item.stripe_subscription_id).delete()
      except stripe.error.CardError, e:
        self.response.out.write(str(e)) 
      except stripe.error.RateLimitError, e:
        self.response.out.write(str(e)) 
      except stripe.error.InvalidRequestError, e:
        self.response.out.write(str(e)) 
      except stripe.error.AuthenticationError, e:
        self.response.out.write(str(e)) 
      except stripe.error.APIConnectionError, e:
        self.response.out.write(str(e)) 
      except stripe.error.StripeError, e:
        self.response.out.write(str(e)) 
      else:
        item.program_status = 'Canceled'
        item.put()
        self.redirect('/cancel_program_success')

def cancelProgram_admin(client_email):
    item = Client_db.get_by_id(client_email)
    if item.program_status == 'Active' and item.stripe_cus_id and item.stripe_subscription_id:
      try:
        customer = stripe.Customer.retrieve(item.stripe_cus_id)
        customer.subscriptions.retrieve(item.stripe_subscription_id).delete()
      except stripe.error.CardError, e:
        return str(e) 
      except stripe.error.RateLimitError, e:
        return str(e) 
      except stripe.error.InvalidRequestError, e:
        return str(e) 
      except stripe.error.AuthenticationError, e:
        return str(e) 
      except stripe.error.APIConnectionError, e:
        return str(e) 
      except stripe.error.StripeError, e:
        return str(e) 
      else:
        item.program_status = 'Canceled'
        item.put()
        return 'success'

class changeProgram(webapp2.RequestHandler):
  def get(self):
    if users.get_current_user():
      program_chosen = self.request.get('program_chosen')
      client_email = users.get_current_user().email()
      item = Client_db.get_by_id(client_email)
      
      try:
        customer = stripe.Customer.retrieve(item.stripe_cus_id)
        subscription= customer.subscriptions.retrieve(item.stripe_subscription_id)
        subscription.plan = program_chosen
        subscription.prorate = False
        subscription.save()
      except stripe.error.CardError, e:
        self.response.out.write(str(e)) 
      except stripe.error.RateLimitError, e:
        self.response.out.write(str(e)) 
      except stripe.error.InvalidRequestError, e:
        self.response.out.write(str(e)) 
      except stripe.error.AuthenticationError, e:
        self.response.out.write(str(e)) 
      except stripe.error.APIConnectionError, e:
        self.response.out.write(str(e)) 
      except stripe.error.StripeError, e:
        self.response.out.write(str(e)) 
      else:
        item.client_program = program_chosen
        item.put()
        
        #--mail to shanny
        message = mail.EmailMessage(sender="Shanny Cohen Fitness <ShannyCohen.Fitness@gmail.com>", subject="Change of Program " + str(item.client_email))    
        message.to = "ShannyCohen.Fitness@gmail.com"
        message.body = "Client: " + str(item.client_name) + "\nEmail: " + str(item.client_email) + "\n\n He/She have changed to:" + "\n " + str(item.client_program) + ' Program \n\n He/She will be billed the amount for the new program in the next bill.'
        message.send()

        self.redirect('/my_account/change_program_success')

class redirect2Payment(webapp2.RequestHandler):
  def get(self):
    program_chosen = self.request.get('program_chosen')
    url = "http://payment.shannycohen.fitness/?program_chosen=" + program_chosen
    self.redirect(str(url), True)

class getCurrentCard(webapp2.RequestHandler):
  def get(self):
    if users.get_current_user():
      client_email = users.get_current_user().email()
      item = Client_db.get_by_id(client_email)
      
      try:
        customer = stripe.Customer.retrieve(item.stripe_cus_id)
        current_card_id = customer.default_source
        current_card = customer.sources.retrieve(current_card_id)
      except stripe.error.CardError, e:
        self.response.out.write(str(e)) 
      except stripe.error.RateLimitError, e:
        self.response.out.write(str(e)) 
      except stripe.error.InvalidRequestError, e:
        self.response.out.write(str(e)) 
      except stripe.error.AuthenticationError, e:
        self.response.out.write(str(e)) 
      except stripe.error.APIConnectionError, e:
        self.response.out.write(str(e)) 
      except stripe.error.StripeError, e:
        self.response.out.write(str(e)) 
      else:
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(current_card['last4'])

class changeCard(webapp2.RequestHandler):
  def post(self):
    if users.get_current_user():
      token = self.request.POST['stripeToken']
      client_email = users.get_current_user().email()
      item = Client_db.get_by_id(client_email)

      try:
        customer = stripe.Customer.retrieve(item.stripe_cus_id)
        card = customer.sources.create(source=token) # create new card
        new_card_id = card.id #get new card id
        customer.default_source = new_card_id #set to default
        customer.save()
      except stripe.error.CardError, e:
        self.response.out.write(str(e)) 
      except stripe.error.RateLimitError, e:
        self.response.out.write(str(e)) 
      except stripe.error.InvalidRequestError, e:
        self.response.out.write(str(e)) 
      except stripe.error.AuthenticationError, e:
        self.response.out.write(str(e)) 
      except stripe.error.APIConnectionError, e:
        self.response.out.write(str(e)) 
      except stripe.error.StripeError, e:
        self.response.out.write(str(e)) 
      else:
        #--mail to client
        message = mail.EmailMessage(sender="Shanny Cohen Fitness <ShannyCohen.Fitness@gmail.com>", subject="Change Credit Card")
        message.to = item.client_email
        message.reply_to = "ShannyCohen.Fitness@gmail.com"
        message.body = "Dear " + str(item.client_name) + ", \n\n You have changed your credit card to: ****" + str(card.last4) + '\n\nShanny Cohen Personal Training LLC.'
        message.send()

        self.redirect('/my_account/change_credit_card_success')

#----------------------------------------------#
#          List and Delete Data                #
#----------------------------------------------#
class deleteData(webapp2.RequestHandler):
    def get(self):
      if users.is_current_user_admin():
        page_address = self.request.uri
        base = os.path.basename(page_address)
        split_address = base.split('?')
        data_set = split_address[1]
        data_id = split_address[2]
    
        if data_set == "exercise":
          item = Exercise_db.get_by_id(data_id)
          if item.exercise_video_key and len(item.exercise_video_key) > 0:
            blobkey = blobstore.blobstore.BlobKey(item.exercise_video_key)
            blobstore.delete(blobkey)

          item.key.delete()
          time.sleep(1)
          self.redirect('/list_data?exercise')

        if data_set == "payment":
          item = Payment_db.get_by_id(data_id)
          item.key.delete()
          time.sleep(1)
          self.redirect('/list_data?payment')

        if data_set == "client":
          item = Client_db.get_by_id(data_id)
          # delete workout plan for this client
          Workout_db._del_client_workout(data_id)

          stripe_remove_msg = 'success'
          if item.program_status == 'Active' and item.stripe_cus_id and item.stripe_subscription_id:
            stripe_remove_msg = cancelProgram_admin(data_id)
          if stripe_remove_msg == 'success':
            item.key.delete()
            time.sleep(1)
            self.redirect('/list_data?client')
          else:
            self.response.out.write("Error! " + stripe_remove_msg) 

        if data_set == "waitlist":
          item = Waitlist_db.get_by_id(data_id)
          item.key.delete()
          time.sleep(1)
          self.redirect('/list_data?waitlist')

        if data_set == "testimonial":
          item = Testimonial_db.get_by_id(data_id)
          item.key.delete()
          time.sleep(1)
          self.redirect('/list_data?testimonial')

        if data_set == "pg_workout":
          item = Workout_db.get_by_id(data_id)
          if item:
            item.key.delete()
            time.sleep(1)
          self.redirect('/list_data?pg_workout')

        if data_set == "sb_workout":
          item = Workout_db.get_by_id(data_id)
          if item:
            item.key.delete()
            time.sleep(1)
          self.redirect('/list_data?sb_workout')

        if data_set == "template":
          item = Template_db.get_by_id(data_id)
          item.key.delete()
          time.sleep(1)
          self.redirect('/list_data?template')

class listData(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        split_address = base.split('?')
        data_set = split_address[1]
        data_id = None
        if len(split_address) == 3:
          data_id = split_address[2]
        
        
        if data_set == 'bikini_bootcamp' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(BikiniBootcamp_db._get_all_data())
        
        if data_set == 'bikini_bootcamp' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(BikiniBootcamp_db._get_one_data(data_id))

# // - Free Weekly Video
    
        if data_set == 'free_weekly' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Weekly_video_db._get_all_data())
        
        if data_set == 'free_weekly' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Weekly_video_db._get_one_data(data_id))
        
        if data_set == 'weekly_video' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Weekly_video_db._get_all_data())
        
        if data_set == 'weekly_video' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Weekly_video_db._get_one_data(data_id))
        
        if data_set == 'homepage_video' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Homepage_video_db._get_all_data())
        
        if data_set == 'homepage_video' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Homepage_video_db._get_one_data(data_id))

        if data_set == 'exercise' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Exercise_db._get_all_data()) 

        if data_set == 'exercise_names' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Exercise_db._get_all_names()) 

        if data_set == 'exercise' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Exercise_db._get_one_data(data_id)) 

        if data_set == 'client' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Client_db._get_all_data()) 

        if data_set == 'pg_client_emails' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Client_db._get_pg_emails()) 

        if data_set == 'client' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Client_db._get_one_data(data_id)) 

        if data_set == 'client_number' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Client_db._count_client()) 

        if data_set == 'current_client' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Client_db._get_current_client())

        if data_set == 'waitlist' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Waitlist_db._get_all_data())

        if data_set == 'waitlist' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Waitlist_db._get_one_data(data_id))

        if data_set == 'current_waitlist' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Waitlist_db._get_current_waitlist())

        if data_set == 'testimonial' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Testimonial_db._get_all_data())

        if data_set == 'testimonial' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Testimonial_db._get_one_data(data_id)) 

        if data_set == 'current_testimonial' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Testimonial_db._get_current_testimonial()) 

        if data_set == 'pg_workout' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Workout_db._get_all_pg_data()) 

        if data_set == 'sb_workout' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Workout_db._get_all_sb_data()) 

        if data_set == 'silver_workout' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Workout_db._get_all_silver_data()) 

        if data_set == 'bronze_workout' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Workout_db._get_all_bronze_data()) 

        if data_set == 'workout' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Workout_db._get_one_data(data_id)) 

        if data_set == 'current_workout' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Workout_db._get_current_workout()) 

        if data_set == 'template' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Template_db._get_all_data()) 

        if data_set == 'template' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Template_db._get_one_data(data_id)) 

        if data_set == 'template_names' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Template_db._get_all_names()) 

#----------------------------------------------#
#             Multi-Media Rendering            #
#----------------------------------------------#
class RenderImg(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        data_set = base.split('?')[1]
        img_size = base.split('?')[2]
        data_id = base.split('?')[3]
        
        if data_set == 'bikini_bootcamp':
          item = BikiniBootcamp_db.get_by_id(data_id)
          img = images.Image(item.video_icon)
        
        if data_set == 'weekly_video':
          item = Weekly_video_db.get_by_id(data_id)
          img = images.Image(item.video_photo)
          
        if data_set == 'homepage_video':
          item = Homepage_video_db.get_by_id(data_id)
          img = images.Image(item.video_icon)

        if data_set == 'exercise':
          item = Exercise_db.get_by_id(data_id)
          img = images.Image(item.exercise_photo)

        if data_set == 'client':
          item = Client_db.get_by_id(data_id)
          img = images.Image(item.client_photo)

        if data_set == 'testimonial':
          item = Testimonial_db.get_by_id(data_id)
          img = images.Image(item.testimonial_photo)

        if img_size == 'thumb':
            img.resize(width=100)
        if img_size == 'small':
            img.resize(width=300)
        if img_size == 'medium':
            img.resize(width=600)
        if img_size == 'large':
            img.resize(width=800)
        image = img.execute_transforms(output_encoding=images.JPEG)
        self.response.headers['Content-Type'] = 'image/jpeg'
        self.response.out.write(image)

class ViewVideo(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, video_key):
        if not blobstore.get(video_key):
            self.error(404)
        else:
            self.send_blob(video_key)

class UploadExerciseVideo(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        try:
            upload = self.get_uploads()[0]
            data_id = self.request.get('data_id')
            item = Exercise_db.get_by_id(data_id)

            if item:
              if item.exercise_video_key and len(item.exercise_video_key) > 0:
                blobkey = blobstore.blobstore.BlobKey(item.exercise_video_key)
                blobstore.delete(blobkey)
                item.exercise_video_key = str(upload.key())
              else:
                item.exercise_video_key = str(upload.key())
              item.put()
              self.redirect('/manage/exercise')
        except:
            self.error(500)

#----------------------------------------------#
#             HTML Page Production             #
#----------------------------------------------#
class publicSite(webapp2.RequestHandler):
    def get(self):
      # - page url
        page_address = self.request.uri
        path_layer = urlparse(page_address)[2].split('/')[1]
        base = os.path.basename(page_address)
      # - user
        user = users.get_current_user()
        if users.get_current_user(): # - logged in
          login_key = users.create_logout_url(self.request.uri)
          gate = 'Sign out'
          user_name = user.email()
        else: # - logged out
          login_key = users.create_login_url(self.request.uri)
          gate = 'Sign in'
          user_name = 'No User'
      # -
        admin = ''
        if users.is_current_user_admin():
            admin = 'true' 
      # - app data
        app = Site
        page_name = 'Main'
        page_id = 'main'
        analytics = Analytics
        nav_html = public_html.public_nav_html
        page_html = page_header + public_html.main_page_html
        html_file = 'publicSite.html'
        nav_select = ''
        
        program_chosen = ''
        data_id = ''
        sub_select = ''
        has_video = 'true'
        
        if path_layer == '':
          html_file = 'fitness_front.html'

# // - Sport Specific

        if path_layer == 'classes':
            page_id = 'sport_specific'
            page_name = 'Sport Specific'
            sub_select = 'snowboarding'
            # page_html = page_header + public_html.sport_specific_snowboarding_page_code
            page_html = ''
            html_file = 'fitness_classes.html'
            nav_select = ''


        if path_layer == 'sport_specific':
            page_id = 'sport_specific'
            page_name = 'Sport Specific'
            sub_select = 'snowboarding'
            # page_html = page_header + public_html.sport_specific_snowboarding_page_code
            page_html = ''
            html_file = 'fitness_classes.html'
            nav_select = ''

            if base == 'motocross':
                sub_select = 'motocross'
                page_html = page_header + public_html.sport_specific_motocross_page_code

            if base == 'skiing':
                sub_select = 'skiing'
                page_html = page_header + public_html.sport_specific_skiing_page_code

            if base == 'snowboarding':
                sub_select = 'snowboarding'
                page_html = page_header + public_html.sport_specific_snowboarding_page_code

            if base == 'soccer':
                sub_select = 'soccer'
                page_html = page_header + public_html.sport_specific_soccer_page_code

            if base == 'surfing':
                sub_select = 'surfing'
                page_html = page_header + public_html.sport_specific_surfing_page_code

            if base == 'more':
                page_html = page_header + public_html.sport_specific_surfing_page_code


        
# // - Public Videos


        if path_layer == 'free_weekly':
            page_id = 'free_weekly'
            page_name = 'Free Weekly'
            page_html = page_header + public_html.free_weekly_page_html
            nav_select = 'free_weekly'
        
        if path_layer == 'bikini_bootcamp':
            page_id = 'bikini_bootcamp'
            page_name = 'Bikini Bootcamp'
            page_html = page_header + public_html.bikini_bootcamp_page_html
            nav_select = 'bikini_bootcamp'
        

# // - Programs Page

        if path_layer == 'join':
            page_id = 'programs'
            page_name = 'Programs'
            page_html = page_header + public_html.programs_page_html
            nav_select = ''

        if path_layer == 'programs':
            page_id = 'programs'
            page_name = 'Programs'
            page_html = page_header + public_html.programs_page_html
            nav_select = ''

        if path_layer == 'results':
            page_id = 'results'
            page_name = 'Results'
            # page_html = page_header + public_html.results_page_html
            page_html = ''
            html_file = 'fitness_results.html'
            nav_select = ''
            
        if path_layer == 'trainers':
            page_id = 'training'
            page_name = 'Training'
            # page_html = page_header + public_html.results_page_html
            page_html = ''
            html_file = 'fitness_training.html'
            nav_select = ''
        
        if path_layer == 'training':
            page_id = 'training'
            page_name = 'Training'
            # page_html = page_header + public_html.results_page_html
            page_html = ''
            html_file = 'fitness_training.html'
            nav_select = ''

        if path_layer == 'exercises':
            page_id = 'exercises'
            page_name = 'Exercises'
            page_html = page_header + workout_html.exercises_page_html
            nav_select = 'exercises'

        if path_layer == 'exercise_detail':
            page_id = 'exercise_detail'
            page_name = 'Exercises'
            page_html = page_header + workout_html.exercise_detail_page_html
            data_id = self.request.get("data_id")
            nav_select = 'exercises'

        if path_layer == 'about':
            page_id = 'about'
            page_name = 'About'
            # page_html = page_header + public_html.about_page_html
            page_html = ''
            html_file = 'about_page.html'
            nav_select = ''


# // - Contact Page

        if path_layer == 'contact':
            page_id = 'contact'
            page_name = 'Contact'
            page_html = page_header + public_html.contact_page_html
            nav_select = ''

        if path_layer == 'contact_success':
            page_id = 'contact_success'
            page_name = 'Contact Success'
            page_html = page_header + public_html.contact_success_page_html
            nav_select = ''


# // - Join Pages

        if path_layer == 'promo_join':
            page_id = 'programs'
            page_name = 'Promo Join'
            page_html = page_header + html.promo_join_page_code
            nav_select = ''

        if path_layer == 'confirm_signup':
            page_id = 'confirm_signup'
            page_name = 'Confirm Signup'
            page_html = page_header + account_html.confirm_signup_page_html
            program_chosen = self.request.get('program_chosen')
            nav_select = ''

        if path_layer == 'payment_success':
            page_id = 'payment_success'
            page_name = 'Payment Success'
            page_html = page_header + account_html.payment_success_page_html
            nav_select = ''

        if path_layer == 'cancel_program_success':
            page_id = 'cancel_program_success'
            page_name = 'Cancel Program Success'
            page_html = page_header + account_html.cancel_program_success_page_html
            nav_select = ''


        if path_layer == 'cam_test':
            page_id = 'cam_test'
            page_name = 'Cam Test'
            page_html = page_header + html.cam_test_page_code
            nav_select = ''

  # - manage, edit, publish pages for public 
        if path_layer == 'manage' or path_layer == 'edit' or path_layer == 'publish':
            page_id = 'login_page'
            page_name = 'Log in'
            page_html = manage_html.manage_page_html
            page_class = 'manage'
            nav_select = ''

  # - some other pages for public 
        if path_layer == 'payment' or path_layer == 'add2waitlist' or path_layer == 'my_account' :
          page_id = 'login_page'
          page_name = 'Log in'
          page_html = page_header + login_page_html
          nav_select = ''

        if user:
          if path_layer == 'payment':
              page_id = 'payment'
              page_name = 'Payment'
              page_html = page_header + account_html.payment_page_html
              program_chosen = self.request.get('program_chosen')
              nav_select = 'my_program'

          if path_layer == 'add2waitlist':
              page_id = 'add2waitlist'
              page_name = 'Add to Waitlist'
              page_html = page_header + account_html.add2waitlist_page_html
              program_chosen = self.request.get('program_chosen')
              nav_select = 'my_program'

          if path_layer == 'my_account':
            if base == 'my_account' or base == '':
              page_id = 'my_account'
              page_name = 'My Account'
              page_html = page_header + account_html.my_account_page_code
              nav_html = account_html.account_nav_html
              nav_select = 'my_account'


            if base == 'my_workout':
              page_id = 'my_workout'
              page_name = 'My Workout'
              page_html = page_header + account_html.my_workout
              nav_html = account_html.account_nav_html
              nav_select = 'my_workout'

            if base.startswith('view_workout'):
              page_id = 'view_my_workout'
              page_name = 'View My Workout Plan'
              page_html = account_html.view_my_workout
              data_id = base.split('?')[1]
              nav_html = account_html.account_nav_html
              nav_select = 'my_workout'

            if base == 'my_library':
              page_id = 'my_library'
              page_name = 'My Library'
              page_html = page_header + account_html.my_library_page_code
              nav_html = account_html.account_nav_html
              nav_select = 'my_library'

            if base == 'my_program':
              page_id = 'my_program'
              page_name = 'My Program'
              page_html = page_header + account_html.my_program_page_code
              nav_html = account_html.account_nav_html
              nav_select = 'my_program'

            if base == 'change_credit_card':
              page_id = 'change_credit_card'
              page_name = 'Change Credit Card'
              page_html = page_header + account_html.change_credit_card_page_html
              nav_html = account_html.account_nav_html
              nav_select = 'my_program'

            if base == 'change_credit_card_success':
              page_id = 'change_credit_card_success'
              page_name = 'Change Credit Card Success'
              page_html = page_header + change_credit_card_success_page_html
              nav_html = account_html.account_nav_html
              nav_select = 'my_program'

            if base == 'change_program_success':
              page_id = 'change_program_success'
              page_name = 'Change Program Success'
              page_html = page_header + change_program_success_page_html
              nav_html = account_html.account_nav_html
              nav_select = 'my_program'

            if base == 'my_info':
              page_id = 'my_info'
              page_name = 'My Info'
              page_html = page_header + account_html.my_info_page_code
              nav_html = account_html.account_nav_html
              nav_select = 'my_info'

            if base == 'edit_my_info':
              page_id = 'edit_my_info'
              page_name = 'Edit My Info'
              page_html = page_header + account_html.edit_my_info_page_code
              nav_html = account_html.account_nav_html
              nav_select = 'my_info'

            if base == 'my_testimonial':
              page_id = 'my_testimonial'
              page_name = 'My Testimonial'
              page_html = page_header + account_html.my_testimonial_page_code
              nav_html = account_html.account_nav_html
              nav_select = 'my_testimonial'

            if base == 'publish_my_testimonial':
              page_id = 'publish_my_testimonial'
              page_name = 'Publish My Testimonial'
              page_html = page_header + account_html.edit_my_testimonial_page_code
              nav_html = account_html.account_nav_html
              nav_select = 'my_testimonial'

            if base.startswith('edit_my_testimonial'):
              page_id = 'edit_my_testimonial'
              page_name = 'Edit My Testimonial'
              page_html = page_header + account_html.edit_my_testimonial_page_code
              nav_html = account_html.account_nav_html
              data_id = base.split('?')[1]
              nav_select = 'my_testimonial'



            
  # - manage, edit, publish pages for admin
        if admin == 'true':

# // Manage Admin --

          if path_layer == 'manage':
              if base == 'manage' or base == '':
                page_id = 'manage'
                page_name = 'Manage'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.manage_page_html
                nav_select = 'manage_page'
              
              if base == 'bikini_bootcamp':
                page_id = 'manage_bikini_bootcamp'
                page_name = 'Manage Bikini Bootcamp'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.manage_bikini_bootcamp_page_html
                nav_select = 'manage_videos'
              
              if base == 'free_weekly':
                page_id = 'manage_free_weekly'
                page_name = 'Manage Free Weekly'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.manage_free_weekly_page_html
                nav_select = 'manage_videos'
              
              if base == 'weekly_video':
                page_id = 'manage_weekly_video'
                page_name = 'Manage Weekly Video'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.manage_weekly_video_page_html
                nav_select = 'manage_videos'
              
              if base == 'homepage_video':
                page_id = 'manage_homepage_video'
                page_name = 'Manage Homepage Video'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.manage_homepage_video_page_html
                nav_select = 'manage_videos'



              if base == 'exercise':
                page_id = 'manage_exercise'
                page_name = 'Manage Exercise'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.manage_exercise_page_html
                nav_select = ''

              if base == 'client':
                page_id = 'manage_client'
                page_name = 'Manage Client'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.manage_client_page_html
                nav_select = 'manage_clients'

              if base == 'waitlist':
                page_id = 'manage_waitlist'
                page_name = 'Manage Waitlist'
                nav_html = manage_html.admin_nav_html
                page_html = manage_waitlist_page_html
                nav_select = 'manage_waitlist'

              if base == 'testimonial':
                page_id = 'manage_testimonial'
                page_name = 'Manage Testimonial'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.manage_testimonial_page_html
                nav_select = 'testimonial'

              if base == 'pg_workout':
                page_id = 'manage_pg_workout'
                page_name = 'Mange Workout'
                nav_html = manage_html.admin_nav_html
                page_html = manage_workout_page_html
                nav_select = 'manage_pg_workout'

              if base == 'sb_workout':
                page_id = 'manage_sb_workout'
                page_name = 'Mange Workout'
                nav_html = manage_html.admin_nav_html
                page_html = manage_workout_page_html
                nav_select = 'manage_sb_workout'

              if base.startswith('view_pg_workout'):
                page_id = 'manage_view_pg_workout'
                page_name = 'View Workout Plan'
                nav_html = manage_html.admin_nav_html
                page_html = manage_view_workout_page_html
                data_id = base.split('?')[1]
                nav_select = ''

              if base.startswith('view_sb_workout'):
                page_id = 'manage_view_sb_workout'
                page_name = 'View Workout Plan'
                nav_html = manage_html.admin_nav_html
                page_html = manage_view_workout_page_html
                data_id = base.split('?')[1]
                nav_select = ''

              if base == 'template':
                page_id = 'manage_template'
                page_name = 'Mange Template'
                nav_html = manage_html.admin_nav_html
                page_html = manage_template_page_html
                nav_select = 'manage_templates'

              if base.startswith('view_template'):
                page_id = 'manage_view_template'
                page_name = 'View Template'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.manage_view_template_page_html
                data_id = base.split('?')[1]
                nav_select = 'manage_templates'

          if path_layer == 'view':
              if base.startswith('client'):
                page_id = 'view_client'
                page_name = 'View Client'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.view_client_page_html
                data_id = base.split('?')[1]
                nav_select = ''


# // Edit Admin --

          if path_layer == 'edit':
              if base == 'edit' or base == '':
                page_id = 'edit'
                page_name = 'Edit'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.manage_page_html
                nav_select = ''
              
              
              if base.startswith('bikini_bootcamp'):
                page_id = 'edit_bikini_bootcamp'
                page_name = 'Edit Bikini Bootcamp'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.publish_bikini_bootcamp_page_html
                data_id = base.split('?')[1]
                nav_select = ''
              
              if base.startswith('free_weekly'):
                page_id = 'edit_free_weekly'
                page_name = 'Edit Free Weekly'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.publish_free_weekly_page_html
                data_id = base.split('?')[1]
                nav_select = ''
              
              if base.startswith('weekly_video'):
                page_id = 'edit_weekly_video'
                page_name = 'Edit Weekly Video'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.publish_weekly_video_page_html
                data_id = base.split('?')[1]
                nav_select = ''
              
              if base.startswith('homepage_video'):
                page_id = 'edit_homepage_video'
                page_name = 'Edit Homepage Video'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.publish_homepage_video_page_html
                data_id = base.split('?')[1]
                nav_select = ''



              if base.startswith('exercise'):
                page_id = 'edit_exercise'
                page_name = 'Edit Exercise'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.edit_exercise_page_html
                data_id = base.split('?')[1]
                nav_select = ''

              if base.startswith('client'):
                page_id = 'edit_client'
                page_name = 'Edit Client'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.edit_client_page_html
                data_id = base.split('?')[1]
                nav_select = ''

              if base.startswith('waitlist'):
                page_id = 'edit_waitlist'
                page_name = 'Edit Waitlist'
                nav_html = manage_html.admin_nav_html
                page_html = edit_waitlist_page_html
                data_id = base.split('?')[1]
                nav_select = ''

              if base.startswith('testimonial'):
                page_id = 'edit_testimonial'
                page_name = 'Edit Testimonial'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.edit_testimonial_page_html
                data_id = base.split('?')[1]
                nav_select = 'testimonial'

              if base.startswith('pg_workout'):
                page_id = 'edit_pg_workout'
                page_name = 'Edit Workout'
                nav_html = manage_html.admin_nav_html
                page_html = edit_workout_page_html
                data_id = base.split('?')[1]
                nav_select = ''

              if base.startswith('sb_workout'):
                page_id = 'edit_sb_workout'
                page_name = 'Edit Workout'
                nav_html = manage_html.admin_nav_html
                page_html = edit_workout_page_html
                data_id = base.split('?')[1]
                nav_select = ''

              if base.startswith('template'):
                page_id = 'edit_template'
                page_name = 'Edit Template'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.edit_template_page_html
                data_id = base.split('?')[1]
                nav_select = ''
              
# // Publish Admin --

          if path_layer == 'publish':



# // Homepage Video --

              if base.startswith('homepage_video'):
                page_id = 'publish_homepage_video'
                page_name = 'Publish Homepage Video'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.publish_homepage_video_page_html
                nav_select = ''

              if base.startswith('homepage_video_upload'):
                page_id = 'homepage_video_upload'
                page_name = 'Publish Homepage Video Upload'
                nav_html = manage_html.admin_nav_html
                upload_url = blobstore.create_upload_url('/upload_homepage_video')
                page_html = manage_html.upload_homepage_video_page_html.format(upload_url)
                data_id = base.split('?')[1]
                nav_select = ''
      
      
          
# // Weekly Video --

              if base.startswith('weekly_video'):
                page_id = 'publish_weekly_video'
                page_name = 'Publish Weekly Video'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.publish_weekly_video_page_html
                nav_select = ''

              if base.startswith('weekly_video_upload'):
                page_id = 'weekly_video_upload'
                page_name = 'Publish Weekly Video Upload'
                nav_html = manage_html.admin_nav_html
                upload_url = blobstore.create_upload_url('/upload_weekly_video')
                page_html = manage_html.upload_weekly_video_page_html.format(upload_url)
                data_id = base.split('?')[1]
                nav_select = ''
                
                
              if base.startswith('free_weekly'):
                page_id = 'publish_free_weekly'
                page_name = 'Publish Free Weekly'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.publish_free_weekly_page_html
                nav_select = ''

              if base.startswith('free_weekly_upload'):
                page_id = 'free_weekly_upload'
                page_name = 'Publish Free Weekly Upload'
                nav_html = manage_html.admin_nav_html
                upload_url = blobstore.create_upload_url('/upload_free_weekly')
                page_html = manage_html.upload_free_weekly_page_html.format(upload_url)
                data_id = base.split('?')[1]
                nav_select = ''
                
                
                
# // Bikini Bootcamp --

              if base.startswith('bikini_bootcamp'):
                page_id = 'publish_bikini_bootcamp'
                page_name = 'Publish Bikini Bootcamp'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.publish_bikini_bootcamp_page_html
                nav_select = ''

              if base.startswith('bikini_bootcamp_upload'):
                page_id = 'bikini_bootcamp_upload'
                page_name = 'Publish Bikini Bootcamp Upload'
                nav_html = manage_html.admin_nav_html
                upload_url = blobstore.create_upload_url('/upload_bikini_bootcamp')
                page_html = manage_html.upload_bikini_bootcamp_page_html.format(upload_url)
                data_id = base.split('?')[1]
                nav_select = ''
            
            
# // Exersise Libary Video --

              if base == 'exercise':
                page_id = 'publish_exercise'
                page_name = 'Publish Exercise'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.edit_exercise_page_html
                nav_select = ''

              if base.startswith('exercise_video'):
                page_id = 'publish_exercise_video'
                page_name = 'Publish Exercise Video'
                nav_html = manage_html.admin_nav_html
                upload_url = blobstore.create_upload_url('/upload_exercise_video')
                page_html = manage_html.publish_exercise_video_page_html.format(upload_url)
                data_id = base.split('?')[1]
                nav_select = ''
            
            
          
# // New Client --

              if base == 'client':
                page_id = 'publish_client'
                page_name = 'Publish Client'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.publish_client_page_html
                nav_select = ''

              if base == 'waitlist':
                page_id = 'publish_waitlist'
                page_name = 'Publish Waitlist'
                nav_html = manage_html.admin_nav_html
                page_html = publish_waitlist_page_html
                nav_select = ''

              if base == 'testimonial':
                page_id = 'publish_testimonial'
                page_name = 'Publish Testimonial'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.edit_testimonial_page_html
                nav_select = 'testimonial'

# // Workouts --

              if base == 'pg_workout':
                page_id = 'publish_pg_workout'
                page_name = 'Publish Workout Plan'
                nav_html = manage_html.admin_nav_html
                page_html = edit_workout_page_html
                nav_select = ''

              if base == 'sb_workout':
                page_id = 'publish_sb_workout'
                page_name = 'Publish Workout Plan'
                nav_html = manage_html.admin_nav_html
                page_html = edit_workout_page_html
                nav_select = ''

              if base == 'template':
                page_id = 'publish_template'
                page_name = 'Publish Template'
                nav_html = manage_html.admin_nav_html
                page_html = manage_html.edit_template_page_html
                nav_select = 'manage_templates'

      # - template
        objects = {
            'Site': app,
            'analytics': analytics,
            'login_key': login_key,
            'gate': gate,
            'user_name': user_name,
            'admin': admin,
          # -
            'path_layer': path_layer,
            'base': base,
            'page_name': page_name,
            'page_id': page_id,
            'nav_html': nav_html,
            'nav_select': nav_select,
            'sub_select': sub_select,
            'page_html': page_html,
            'data_id': data_id,
            'program_chosen': program_chosen,
            'has_video': has_video
        }
      # - render
        path = os.path.join(os.path.dirname(__file__), 'html/%s' %html_file)
        self.response.out.write(template.render(path, objects))







#----------------------------------------------#
#           Weekly Data Stucture               #
#----------------------------------------------#
class Weekly_video_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_date = ndb.StringProperty()
    video_week = ndb.StringProperty()
    video_type = ndb.StringProperty()
    video_class = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_photo = ndb.BlobProperty()
    video_key = ndb.StringProperty()
  #
    current_video = ndb.StringProperty()

    @classmethod
    def _get_all_data(self):
        q = ndb.gql('SELECT data_id, video_date, video_week, user_name, video_id, video_name, video_text, video_key FROM Weekly_video_db')
        db_data = []
        for item in q.iter():
          db_data.append({'data_id': item.data_id, 'video_date': item.video_date, 'video_week': item.video_week, 'user_name': item.user_name, 'video_id': item.video_id, 'video_name': item.video_name, 'video_text': item.video_text, 'video_key': item.video_key})
        return json.dumps(db_data)

    @classmethod
    def _get_one_data(self,data_id):
        # item = Exercise_db.get_by_id(data_id)
        q =ndb.gql('SELECT user_name, video_id, video_name, video_text, video_key FROM Weekly_video_db WHERE data_id= :1', data_id)

        db_data={}
        for item in q:
          db_data = {'data_id': data_id, 'video_id': item.video_id, 'video_name': item.video_name, 'video_text': item.video_text}
        return json.dumps(db_data)

    @classmethod
    def _get_all_names(self):
        q =ndb.gql('SELECT data_id, exercise_name from Weekly_video_db')
        db_data = {}
        for item in q.iter():
          db_data[item.data_id] = item.exercise_name
        return json.dumps(db_data)

class setWeekly_video_db(webapp2.RequestHandler):
  def post(self):

    if users.is_current_user_admin():
      old_video = Weekly_video_db.all().filter('current_video =', 'current')
      old_video.current_video = '-'
      old_video.put()
      data_id = self.request.get('data_id')
      if data_id and data_id != '':
        item = Weekly_video_db.get_by_id(data_id)
        item.current_video = 'current'
        item.put()
        self.response.out.write('set current to ' + item.video_name)



class addWeekly_video_db(webapp2.RequestHandler):
  def post(self):

    if users.is_current_user_admin():
      data_id = self.request.get('data_id')
      if data_id and data_id != '':
        item = Weekly_video_db.get_by_id(data_id)
      else:
        data_id = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d%H%M%S")
        item = Weekly_video_db(id=data_id)
        item.data_id = data_id
      # - -
      item.user_name = users.get_current_user().nickname()
      item.video_id = data_id
      item.video_name = self.request.get('video_name')
      item.video_text = self.request.get('video_text')
      item.video_type = 'weekly_video'
      item.video_class = 'public'
      item.current_video = '-'
      
      item.video_date = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%b %d %Y")
      item.video_week = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%U")

      
      image_file = self.request.get('image_file')
      if image_file:
        item.video_photo = images.resize(image_file, 800, 600)
      #
      item.put()
      time.sleep(1)
      self.redirect('/publish/weekly_video_upload?{0}'.format(data_id))

class UploadWeeklyVideo(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        try:
            upload = self.get_uploads()[0]
            data_id = self.request.get('data_id')
            item = Weekly_video_db.get_by_id(data_id)

            if item:
              if item.video_key and len(item.video_key) > 0:
                blobkey = blobstore.blobstore.BlobKey(item.video_key)
                blobstore.delete(blobkey)
                item.video_key = str(upload.key())
              else:
                item.video_key = str(upload.key())
              item.put()
              self.redirect('/manage/weekly_video')
        except:
            self.error(500)



class adminSite(webapp2.RequestHandler):
    def get(self):
      # - page url
        page_address = self.request.uri
        path_layer = urlparse(page_address)[2].split('/')[1]
        base = os.path.basename(page_address)
      # - user
        user = users.get_current_user()
        if users.get_current_user(): # - logged in
          login_key = users.create_logout_url(self.request.uri)
          gate = 'Sign out'
          user_name = user.email()
        else: # - logged out
          login_key = users.create_login_url(self.request.uri)
          gate = 'Sign in'
          user_name = 'No User'
      # -
        admin = ''
        if users.is_current_user_admin():
            admin = 'true' 
      # - app data
        app = Site
        page_name = 'Main'
        page_id = 'main'
        analytics = Analytics
        nav_html = manage_html.admin_nav_html
        page_html = manage_html.manage_page_html
        html_file = 'adminSite.html'
        
        program_chosen = ''
        data_id = ''
        sub_select = ''


        if path_layer == 'manage':
            page_name = 'Manage Videos'
            page_html = manage_html.manage_page_html

            if base == 'videos':
                page_id = 'manage_videos'
                page_html = manage_html.manage_videos_page_html


      # - template
        objects = {
            'Site': app,
            'analytics': analytics,
            'login_key': login_key,
            'gate': gate,
            'user_name': user_name,
            'admin': admin,
          # -
            'path_layer': path_layer,
            'base': base,
            'page_name': page_name,
            'page_id': page_id,
            'nav_html': nav_html,
            'sub_select': sub_select,
            'page_html': page_html,
            'data_id': data_id,
            'program_chosen': program_chosen,     
        }
      # - render
        path = os.path.join(os.path.dirname(__file__), 'html/%s' %html_file)
        self.response.out.write(template.render(path, objects))







#----------------------------------------------#
#            Error Handling                    #
#----------------------------------------------#
def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('A 404 error occurred!')
    response.set_status(404)

def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('A 500 error occurred!')
    response.set_status(500)
#----------------------------------------------#
#                                              #
#----------------------------------------------#
app = webapp2.WSGIApplication([    # - Pages

    ('/', publicSite),

    ('/cam_test/?', publicSite),
    
    ('/join/?', publicSite),
    ('/programs/?', publicSite),
      ('/confirm_signup/?', publicSite),
      ('/redirect2payment/?', redirect2Payment),
      ('/payment/?', publicSite),
      ('/charge_card/?', chargeCard),
      ('/payment_success', publicSite),
      ('/cancel_program/?', cancelProgram),
      ('/cancel_program_success/?', publicSite),
      ('/change_current_program/?', changeProgram),
      ('/change_card/?', changeCard),

      ('/add2waitlist/?', publicSite),

    ('/my_account/?', publicSite),
    ('/my_account/my_program/?', publicSite),
    ('/my_account/my_info/?', publicSite),
    ('/my_account/my_testimonial/?', publicSite),
    ('/my_account/my_workout/?', publicSite),
    ('/my_account/my_library/?', publicSite),
    ('/my_account/view_workout/?', publicSite),
    ('/my_account/edit_my_info/?', publicSite),
    ('/my_account/add_my_info/?', addClient_db_user),
    ('/my_account/publish_my_testimonial/?', publicSite),
    ('/my_account/edit_my_testimonial/?', publicSite),
    ('/my_account/change_credit_card/?', publicSite),
    ('/get_current_card/?', getCurrentCard),
    ('/my_account/change_program_success/?', publicSite),
    ('/my_account/change_credit_card_success/?', publicSite),

    ('/bikini_bootcamp/?', publicSite),
    ('/free_weekly/?', publicSite),
    ('/results/?', publicSite),
    ('/trainers/?', publicSite),
    ('/training/?', publicSite),
    ('/exercises/?', publicSite),
      ('/exercise_detail/?', publicSite),
    ('/about/?', publicSite),
    ('/classes/?', publicSite),
    ('/classes/?', publicSite),
    ('/sport_specific/?', publicSite),
      ('/sport_specific/motocross/?', publicSite),
      ('/sport_specific/skiing/?', publicSite),
      ('/sport_specific/snowboarding/?', publicSite),
      ('/sport_specific/soccer/?', publicSite),
      ('/sport_specific/surfing/?', publicSite),
      ('/sport_specific/more/?', publicSite),


    ('/promo_join/?', publicSite),

    ('/contact/?', publicSite),
    ('/verify_recaptcha/?', verifyRecaptcha),
    ('/submit_question/?', submitQuestion),
    ('/contact_success/?', publicSite),

    ('/manage/?', publicSite),
    ('/manage/bikini_bootcamp/?', publicSite),
    ('/manage/weekly_video/?', publicSite),
    ('/manage/homepage_video/?', publicSite),
    ('/manage/videos/?', adminSite),
    ('/manage/exercise/?', publicSite),
    ('/manage/client/?', publicSite),
    ('/manage/waitlist/?', publicSite),
    ('/manage/testimonial/?', publicSite),
    ('/manage/pg_workout/?', publicSite),
    ('/manage/sb_workout/?', publicSite),
    ('/manage/view_pg_workout/?', publicSite),
    ('/manage/view_sb_workout/?', publicSite),
    ('/manage/template/?', publicSite),
    ('/manage/view_template/?', publicSite),

    ('/edit/?', publicSite),
    ('/edit/bikini_bootcamp/?', publicSite),
    ('/edit/weekly_video/?', publicSite),
    ('/edit/homepage_video/?', publicSite),
    ('/edit/exercise/?', publicSite),
    ('/edit/client/?', publicSite),
    ('/edit/waitlist/?', publicSite),
    ('/edit/testimonial/?', publicSite),
    ('/edit/pg_workout/?', publicSite),
    ('/edit/sb_workout/?', publicSite),
    ('/edit/template/?', publicSite),

    ('/view/client/?', publicSite),

    
    
    ('/publish/bikini_bootcamp/?', publicSite),
    ('/publish/bikini_bootcamp_upload/?', publicSite),
    ('/publish/free_weekly/?', publicSite),
    ('/publish/free_weekly_upload/?', publicSite),
    
    ('/publish/weekly_video/?', publicSite),
    ('/publish/weekly_video_upload/?', publicSite),
    ('/publish/homepage_video/?', publicSite),
    ('/publish/homepage_video_upload/?', publicSite),
    ('/publish/exercise/?', publicSite),
    ('/publish/exercise_video?', publicSite),
    ('/publish/client/?', publicSite),
    ('/publish/waitlist/?', publicSite),
    ('/publish/testimonial/?', publicSite),
    ('/publish/pg_workout/?', publicSite),
    ('/publish/sb_workout/?', publicSite),
    ('/publish/template/?', publicSite),

# - Admin

    
    ('/manage/add_bikini_bootcamp/?', addBikiniBootcamp_db),
    ('/upload_bikini_bootcamp/?', UploadBikiniBootcampVideo),
    
    ('/manage/add_weekly_video/?', addWeekly_video_db),
    ('/upload_weekly_video/?', UploadWeeklyVideo),
    ('/manage/add_homepage_video/?', addHomepage_video_db),
    ('/upload_homepage_video/?', UploadHomepageVideo),
    ('/manage/add_exercise/?', addExercise_db),
    ('/upload_exercise_video/?', UploadExerciseVideo),
    ('/manage/add_client/?', addClient_db),
    ('/manage/add_waitlist/?', addWaitlist_db),
    ('/manage/add_testimonial/?', addTestimonial_db),
    ('/manage/add_workout/?', addWorkout_db),
    ('/manage/add_template/?', addTemplate_db),

    # ('/manage/add_client/?', addClient_db),
    ('/list_data/?', listData),
    # ('/code/?', codePage),
    ('/delete_data/?', deleteData),
    ('/render_img/?', RenderImg),
    ('/view_video/([^/]+)?', ViewVideo),

], debug=True)
# app.error_handlers[404] = handle_404
# app.error_handlers[500] = handle_500
