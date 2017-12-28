# -*- coding: latin-1 -*-
# - HTML Page Code



account_nav_html = '''
  <nav class="main_nav">
    <ul>
      <a href="../../my_account/my_info"><li id="my_infoNav">My Info</li></a>
      <a href="../../my_account/"><li id="my_accountNav">My Account</li></a>
      <a href="../../my_account/my_program"><li id="my_programNav">My Program</li></a>
      <a href="../../my_account/my_testimonial"><li id="my_testimonialNav">My Results</li></a>
      <a href="../../my_account/my_workout"><li id="my_workoutNav">My Workout</li></a>
      <a href="../../my_account/my_library"><li id="my_libraryNav">My Library</li></a>
    </ul>
  </nav><!-- - /main_nav - -->
'''


my_library_page_code = '''<style>
body { background: url("../../pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }

header { background: rgba(0,0,0, 0.6); color: #fff; }

</style>
  <div class="main_wrap-[!layout_style!]">


  </div><!-- .main_wrap -->
'''

my_account_page_code = '''<style>
body { background: url("../../pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }

header { background: rgba(0,0,0, 0.6); color: #fff; }

.list_wrap { max-width: 550px; margin: 0 auto; border-left: 1px solid #ddd; border-right: 1px solid #ddd; padding: 15px; background:rgba(0,0,0, 0.6); color: #fff; }
.list_wrap-mobile { }
.list_wrap-desktop {  min-width: 350px; }


.option_wrap { border-bottom: 1px solid #fff; padding: 25px; }
.option_wrap a { color: #fff; }

.option_wrap:hover { border-bottom: 1px solid #aaa; padding: 25px; }
.option_wrap a:hover { color: #ddd; }


</style>
  <div class="main_wrap-[!layout_style!]">

    <header class="my_account_header_wrap">
      <div class="user_photo">
        <img ng-src="/render_img?client?thumb?[! user_name !]">
      </div><!-- . user_photo -->
      <div class="account_user_welcome">
        <p><span style="font-size:28px;">Hello [!client_name!],</span><p>
        </p>My Account</p>
        <div class="header_user_name">[!user_name!]</div>
      </div>
    </header><!-- . my_account_header_wrap - -->

    <div class="list_wrap list_wrap-[!layout_style!]">
      <div class="option_wrap">
        <a href="/my_account/my_workout">My Workout Plan</a>
        <a href="/my_account/my_workout"><button>Open</button></a>
      </div>
      <div class="option_wrap">
        <a href="/my_account/my_info">My Info</a>
        <a href="/my_account/my_info"><button>Open</button></a>
      </div>
      <div class="option_wrap">
        <a href="/my_account/my_program">My Program</a>
        <a href="/my_account/my_program"><button>Open</button></a>
      </div>
      <div class="option_wrap">
        <a href="/my_account/my_testimonial">My Results</a>
        <a href="/my_account/my_testimonial"><button>Open</button></a>
      </div>
      
    </div><!-- .list_wrap -->



  </div><!-- .main_wrap -->
'''




my_workout = '''<style>
body { background: rgba(0,0,0, 0.3); }

header { background: rgba(0,0,0, 0.6); color: #fff; }

.list_wrap { max-width: 550px; margin: 0 auto; border-left: 1px solid #ddd; border-right: 1px solid #ddd; padding: 15px; background:rgba(0,0,0, 0.6); color: #fff; font-size: 14px; }
.list_wrap-mobile { }
.list_wrap-desktop { min-width: 350px; }
.option_wrap span { color: red; }
.option_wrap span.label { color: #aaa; }

.item_name { font-size: 20px; line-height: 16px; }

.option_wrap { border-bottom: 1px solid #fff; padding: 10px; }
.option_wrap a { color: #fff; }

.option_wrap:hover { border-bottom: 1px solid #aaa; }
.option_wrap a:hover { color: #ddd; }
.option_wrap button { float: right; }

.text_wrap { display: inline-block; }
.button_wrap { display: inline-block; outline: 1px solid #333; float: right;  padding: 10px; padding-top: 25px; min-height: 50px;  }

</style>
  <div class="main_wrap-[!layout_style!]">

    <header class="my_account_header_wrap">
      <div class="user_photo">
        <img ng-src="/render_img?client?thumb?[! user_name !]">
      </div><!-- . user_photo -->
      <div class="account_user_welcome">
        <p><span style="font-size:28px;">Hello [!client_name!],</span><p>
        </p>My &nbsp; Workout Plans</p>
        <div class="header_user_name">[!user_name!]</div>
      </div>
    </header><!-- . my_account_header_wrap - -->

  <div class="list_wrap list_wrap-[!layout_style!]">
    
    <div class="option_wrap" ng-repeat="item in workout_data | orderBy: '-add_time'">
      <div class="text_wrap">
     
        <p class="item_name">[! item.template_name!]</p>
        <p><span class="label">Explanation</span> &nbsp; <span>|</span> &nbsp;  [! item.general_explanation!]</p>
        <p><span class="label">Add Time</span> &nbsp; <span>|</span> &nbsp; [! item.add_time!]</p>
      </div>

        <div class="button_wrap">
          <a ng-href='/my_account/view_workout?[!item.data_id!]'><button>Open</button></a>
        </div>

         
      
    </div><!-- . option_wrap - -->
      
    </div><!-- .list_wrap -->
  </div><!-- .main_wrap -->
'''


view_my_workout = '''
<style type="text/css">
  body { background: rgba(0,0,0, 0.3); }
  header { background: rgba(0,0,0, 0.6); color: #fff; }
    .main_wrap a { text-decoration: underline; }
    .outter_wrap { }
    #workout_plan { table-layout: fixed; background-color: #fff; padding: 10px; }
    #workout_plan th { background:#37474F; color: #fff; padding: 5px; min-width: 100px; font-size: 14px;}
    #workout_plan td { padding: 5px; min-width: 100px; font-size: 18px; }
    .White, .Red, .Orange, .LightBlue, .LightGreen, .LightGrey, .BlueGrey { border:1px solid grey; padding: 10px 10px; margin: 5px auto;}
    .White { background:#fff;}.Red{background:#FFCDD2;}.Orange{background:#FFE0B2;}.LightBlue{background:#81D4FA;}.LightGreen{background:#B2DFDB;}.LightGrey{background:#E0E0E0;}.BlueGrey{background:#B0BEC5;}
    pre { white-space: pre-wrap; white-space: -moz-pre-wrap; white-space: -pre-wrap;  white-space: -o-pre-wrap; word-wrap: break-word;}
    .note_text { font-size: 12px; }
    
    td.image { width:110px; text-align: center; }
    td.exercise { text-align:left; }

    .item_wrap { display: inline-block; padding: 15px; margin: 5px; width: 150px; vertical-align: top; padding-bottom: 125px; padding-top: 10px; }

    .item_data { position: relative; ; width: 150px; }

    .item_name { height: 45px; margin-bottom: 5px; }

    .set_wrap { font-family: Consolas, monospace; font-size: 12px; }

    .set_item { border-top: 1px solid #bbb; height: 60px; margin-bottom: 10px; padding-top: 10px; margin-top: 5px; }
    .set_name { text-align: center; margin-bottom: 10px; }
    .set_image { text-align: center; }
    .set_image img { width: 85%; }
    .set_note { font-size: 12px; min-height: 115px; margin-top: 15px; }
    .set_data { text-align: left; margin-top: 5px; color: black;  }

</style>
<div class="main_wrap-[!layout_style!]">
  <header class="my_account_header_wrap">
    <div class="user_photo">
      <img ng-src="/render_img?client?thumb?[! user_name !]">
    </div><!-- . user_photo -->
    <div class="account_user_welcome">
      <p><span style="font-size:28px;">Hello [!client_name!],</span><p>
      </p>My &nbsp; Workout Plan</p>
      <div class="header_user_name">[!user_name!]</div>
    </div>
  </header><!-- . my_account_header_wrap - -->
  <a ng-href='/my_account/my_workout'><button>Back</button></a>

  <button ng-click="print_workout()">Print</button>

   <p id="print_line1">[!item.program_date!]&nbsp;&nbsp;[!item.muscles!]&nbsp;&nbsp;[!item.client_email!]</p>
  <p id="print_line2">[!item.general_explanation!]</p>



  <div class="outter_wrap">
    <div class="item_wrap" ng-repeat="exercise in item.workout" ng-class="exercise.exercise_color">
      <div class="item_data">
        <div class="item_name"><a href="/exercise_detail/?data_id=[!exercise.exercise_id!]" target="_blank">[!exercise.name!]</a></div>
        <div class="set_image">
          <img ng-src="/render_img?exercise?thumb?[!exercise.exercise_id!]"></div>

  <div class="set_note">[!exercise.notes!]</div>
  

      <div class="set_wrap">

        <div class="set_item">
          <div class="set_name">Warm Up</div>
          <div class="set_data">[!exercise.warmup_set!]</div>
        </div>

        <div class="set_item">
          <div class="set_name">Set 1</div>
          <div class="set_data">[!exercise.set1!]</div>
        </div>

        <div class="set_item">
          <div class="set_name">Set 2 </div>
          <div class="set_data">[!exercise.set2!]</div>
        </div>

        <div class="set_item">
           <div class="set_name">Set 3</div>
           <div class="set_data">[!exercise.set3!]</div>
         </div>

        <div class="set4 set_item" ng-show="table_length>=4">
           <div class="set_name">Set 4</div>
           <div class="set_data">[!exercise.set4!]</div>
         </div>

        <div class="set5 set_item"  ng-show="table_length>=5">
           <div class="set_name">Set 5 </div>
           <div class="set_data">[!exercise.set5!]</div>
        </div>

      </div><!-- . set_wrap - -->
   
    </div>
  </div><!-- .item_wrap -->

    </div><!-- .outter_wrap -->




  <div class="outter_wrap">
    <table id="workout_plan">

      <tr>
        <th>Image</th>
        <th>Exercise</th>
        <th>Warm up sets</th>
        <th>Set 1</th>
        <th>Set 2</th>
        <th>Set 3</th>
        <th class="set4" ng-show="table_length>=4">Set 4</th>
        <th class="set5" ng-show="table_length>=5">Set 5</th>
      </tr>

      <tr ng-repeat="exercise in item.workout" ng-class="exercise.exercise_color">
            <td class="image"><img style="width:100px;" ng-src="/render_img?exercise?thumb?[!exercise.exercise_id!]"></td>
            <td class="exercise"><a href="/exercise_detail/?data_id=[!exercise.exercise_id!]" target="_blank">[!exercise.name!]</a><br><span class="note_text">[!exercise.notes!]</span></td>
            <td><pre>[!exercise.warmup_set!]</pre></td>
            <td><pre>[!exercise.set1!]</pre></td>
            <td><pre>[!exercise.set2!]</pre></td>
            <td><pre>[!exercise.set3!]</pre></td>
            <td class="set4" ng-show="table_length>=4"><pre>[!exercise.set4!]</pre></td>
            <td class="set5"  ng-show="table_length>=5"><pre>[!exercise.set5!]</pre></td>
      </tr><!-- .exercise_list -->

    </table>
    </div><!-- .outter_wrap -->

    <button ng-click="print_workout()">Print</button>
    <p>For Firefox and IE users to print the background color, please check the “Print Background Colors” on the Print dialog that is popped up.</p>
  </div><!-- .main_wrap -->

'''




my_program_page_code = ''' 
  <style>
  body { background: rgba(0,0,0, 0.3); }
header { background:rgba(0,0,0, 0.6); color: #fff; }

.main_wrap1 { background:rgba(0,0,0, 0.6); color: #fff; padding: 15px; }

  .change_program_btn { margin: 10px auto; }
  .red { color: red; }
  .label { color: #999; }

  </style>
  <div class="main_wrap-[!layout_style!]">

    <header class="my_account_header_wrap">
      <div class="user_photo">
        <img ng-src="/render_img?client?thumb?[! user_name !]">
      </div><!-- . user_photo -->
      <div class="account_user_welcome">
        <p><span style="font-size:28px;">Hello [!client_name!],</span><p>
        </p>My Account</p>
        <div class="header_user_name">[!user_name!]</div>
      </div>
    </header><!-- . my_account_header_wrap - -->

    <div class="main_wrap1">
      <p><span class="label">Program</span> &nbsp; <span class="red">|</span> &nbsp; [!client_program!]</p> 
      <p ng-show='program_status'><span class="label">Program Status</span> &nbsp; <span class="red">|</span> &nbsp; [!program_status !]</p>
        <span ng-show="program_status!='Canceled'&&client_program&&stripe_cus_id&&stripe_subscription_id"></span> 
        <p class="btn_wrap">
          <button ng-disabled="btn_disable" ng-click="">Pause Program</button>
          <button ng-disabled="btn_disable" ng-click="cancel_program()">Cancel Program</button>
          <button ng-disabled="btn_disable" ng-click="program_list_show = program_list_show? false: true;">Change Program</button>
          <a href="/my_account/change_credit_card"><button ng-disabled="btn_disable">Change Credit Card</button></a>
        </p>

        <div class="change_program_btn" ng-repeat='(key,value) in program_price_list'>
          <button ng-disabled="btn_disable" ng-click="change_program(key)" ng-show='program_list_show&&key!=client_program'>[!key!]($[!value!]/month)</button>
        </div><!--.change_program_btn -->
        <hr>
    <div>
      <p>Waitlist: [!client_waitlist!]</p>
        <p ng-show='client_waitlist'>Since: [!waitlist_add_time | limitTo: 10!]</p> 
    </div>

    </div><!-- . main_wrap1 - -->
    
  </div><!-- . main_wrap -->
'''


my_info_page_code = '''
  <style type="text/css">
body { background: rgba(0,0,0, 0.3); }

header { background: rgba(0,0,0, 0.6); color: #fff; }

.my_info_wrap { max-width: 400px; margin: 0 auto; margin-top: 15px;  }
.my_info_data { border: 1px solid #fff; border-radius: 3px; text-align: left; background: rgba(0,0,0, 0.6); color: #fff; padding: 15px; }

.img_wrap { text-align: center; margin-top: 20px; }
.text_wrap { width: 75%; margin: 0 auto; }

.red { color: red; }
.label { color: #999; }

.edit_button_wrap { text-align: center; margin-bottom: 15px; margin-top: 30px; }

@media screen and (min-width: 800px){
      .client_data {  }
    }


  </style>
<div class="main_wrap-[!layout_style!]">
  <div class="my_info_wrap">
    <div class="my_info_data">

      <div class="img_wrap">
        <img ng-src="[! item.has_photo?'/render_img?client?thumb?'+item.client_email : '' !]">
      </div><!--.img_wrap-->

      <div class="text_wrap">
        <p><span class="label">Name</span> &nbsp; <span class="red">|</span> &nbsp; [! item.client_name !]</p>
        <p><span class="label">Phone</span> &nbsp; <span class="red">|</span> &nbsp; [! item.client_phone !]</p> 
        <p><span class="label">Address</span> &nbsp; <span class="red">|</span> &nbsp; [! item.client_address !]</p> 
      </div><!--.text_wrap-->


      <div class="edit_button_wrap">
        <a ng-href='/my_account/edit_my_info'><button ng-disabled="btn_disable">Edit Info</button></a>
      </div><!-- . edit_button_wrap - -->

    </div><!--.my_info_data-->
  </div><!-- . my_info_wrap - -->
</div><!-- .main_wrap -->
'''


edit_my_info_page_code = '''
  <style>
body { background: rgba(0,0,0, 0.3); }

header.hi { color: #000; }


.my_info_wrap { max-width: 400px; margin: 0 auto; margin-top: 15px; padding-bottom: 75px; }
.my_info_data { border: 1px solid #fff; border-radius: 3px; text-align: left; background: rgba(0,0,0, 0.6); color: #fff; padding: 15px; }

.img_wrap { text-align: center; margin-top: 20px; margin-bottom: 15px; }
.red { color: red; }

table { border-spacing: 10px; }
tr { height: 32px; }
td.label { font-size: 14px; text-align: right; padding-right: 10px; border-right: 1px solid red; color: #999; }
td.input { padding-left: 10px; }
td img{ max-width: 70px; }
input[type="text"] { width: 200px; height: 18px; }

.edit_button_wrap { text-align: center; margin-bottom: 15px; margin-top: 30px; }

  </style>
  <div class="main_wrap-[!layout_style!]">
   <header class="hi"><span class="color_b">Edit My Info</span></header>

  <div class="my_info_wrap">
    <div class="my_info_data">


      <form action="/my_account/add_my_info" enctype="multipart/form-data" method="post">
        <div class="img_wrap">
          <img ng-src="[! item.has_photo?'/render_img?client?thumb?'+item.client_email : '' !]">
        </div><!--.img_wrap-->
        <table>
          <tr class="hide">
            <td class="label">Email</td>
            <td class="input"><input type="text" name="client_email" ng-model='item.client_email' required/></td>
          </tr>
          <tr>
            <td class="label">Name</td>
            <td class="input"><input type="text" name="client_name" ng-model='item.client_name' required/></td>
          </tr>
          <tr>
            <td class="label">Phone</td>
            <td class="input"><input type="text" name="client_phone" ng-model='item.client_phone'/></td>
          </tr>
          <tr>
            <td class="label">Address</td>
            <td class="input"><input type="text" name="client_address" ng-model='item.client_address'/></td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><input type="file" name="client_photo"/></td>
          </tr>

        </table>

        <div class="edit_button_wrap">
        <a href="/my_account/my_info"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
      </div><!-- . edit_button_wrap - -->


      </form>

    </div><!--.my_info_data-->
  </div><!-- . my_info_wrap - -->
</div><!-- - .main_wrap - -->
'''



my_testimonial_page_code = '''
  <style type="text/css">
    body { background: rgba(0,0,0, 0.3); }

header { background:rgba(0,0,0, 0.6); color: #fff; }
    pre{ white-space: pre-wrap; white-space: -moz-pre-wrap; white-space: -pre-wrap;  white-space: -o-pre-wrap; word-wrap: break-word;}
    .testimonial_wrap { border: 1px solid #fff; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px; background:rgba(0,0,0, 0.6); color: #fff; }
    .show_btn{color: steelblue;}
    .testimonial_thumb { max-width: 100px; }
    .modal-backdrop { position: fixed; top: 0; left: 0; bottom: 0; right: 0;  z-index: 150;  background:rgba(0,0,0, 0.6);}
    .modal { position: absolute; top:25px; z-index: 200; text-align: center; margin: auto auto; }
    #lg_img { max-height: 600px; max-width: 800px; margin: auto auto; }
    </style>
  <div class="main_wrap-[!layout_style!]">

    <header class="my_account_header_wrap">
      <div class="user_photo">
        <img ng-src="/render_img?client?thumb?[! user_name !]">
      </div><!-- . user_photo -->
      <div class="account_user_welcome">
        <p><span style="font-size:28px;">Hello [!client_name!],</span><p>
        </p>My Account</p>
        <div class="header_user_name">[!user_name!]</div>
      </div>
    </header><!-- . my_account_header_wrap - -->

    <a href='/my_account/publish_my_testimonial'><button>Add A New Testimonial</button></a>
    <hr>

    <div class="modal-backdrop" ng-show="modal_show"></div>
    <div class="modal" ng-show="modal_show">
      <img id="lg_img" ng-src='[!lg_img_url!]'>
      <button ng-click="hide_lg_img()">Close</button>
    </div>

    <div class="testimonial_wrap" ng-repeat="item in testimonial_data">
      <testimonial-view data="item"></testimonial-view>
      <br>
      <a ng-href='/my_account/edit_my_testimonial?[!item.data_id!]'><button>Edit Info</button></a>
      <button ng-click="delete(item.data_id)">Remove</button>
    </div><!-- .testimonial_wrap -->
  </div><!-- . main_wrap - -->
'''


edit_my_testimonial_page_code = '''
  <style>
body { background: rgba(0,0,0, 0.3); }

header.hi { color: #000; }


.my_info_wrap { max-width: 400px; margin: 0 auto; margin-top: 15px; padding-bottom: 75px; }
.my_info_data { border: 1px solid #fff; border-radius: 3px; text-align: left; background: rgba(0,0,0, 0.6); color: #fff; padding: 15px; }

.img_wrap { text-align: center; margin-top: 20px; margin-bottom: 15px; }
.red { color: red; }

table { border-spacing: 10px; }
tr { height: 32px; }
td.label { font-size: 14px; text-align: right; padding-right: 10px;color: #999; }
td.input { }
td img{ max-width: 70px; }
input[type="text"] { width: 200px; height: 18px; }

.edit_button_wrap { text-align: center; margin-bottom: 15px; margin-top: 30px; }

  </style>
  <div class="main_wrap-[!layout_style!]">
   <header class="hi" ng-show="!if_edit"><span class="color_b">Add New Testimonial</span></header>
   <header class="hi" ng-show="if_edit"><span class="color_b">Edit Testimonial</span></header>
  <div class="my_info_wrap">
    <div class="my_info_data">
      <form action="/manage/add_testimonial" enctype="multipart/form-data"  method="post">
        <table>
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' ng-required="if_edit" ></td>
          </tr>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" ng-model="item.client_name" required/></td>
          </tr>
          <tr>
            <td class="label">Comment*</td>
            <td class="input"><textarea rows="20" cols="32" name="testimonial_text"  ng-model="item.testimonial_text" required></textarea></td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><input type="file" name="testimonial_photo"/></td>
          </tr>
          <tr ng-if="item.has_photo">
            <td class="label">
             <img ng-src="[! item.has_photo?'/render_img?testimonial?thumb?'+item.data_id : '' !]">
             </td>
            <td class="input"></td>    
          </tr>     

        </table>

        <div class="edit_button_wrap">
        <a href="/my_account/my_testimonial"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
      </div><!-- . edit_button_wrap - -->


      </form>
    </div><!--.my_info_data-->
  </div><!-- . my_info_wrap - -->
  </div><!-- - .main_wrap - --> 
'''


confirm_signup_page_html = '''<style>
body { background: url("../../pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }
.content_wrap { background-color: rgba(0,0,0, 0.6); color: #fff; text-align: center; padding: 20px; width: 425px; margin: 0 auto; }
.content_wrap span { font-size: 24px; }

</style>
  <div class="main_wrap-[!layout_style!]">
    <div class="content_wrap">
    <p><span>You have chosen the [!program_chosen!] Program</span><br />($[!price!]/month)</p>
    <button ng-click="back2programs();">Cancel</button>
    <button ng-click="go2payment();">Go to Payment</button>
  </div><!-- . main_wrap -->
'''




change_credit_card_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px;text-align:center;}
  form{padding: 15px 45px;}
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td.input { font-size: 14px; text-align: left; padding-left: 10px; }
  .form_title{background: #0D47A1; padding: 10px; color:#fff;}
  .payment-errors{color:red;}
  .stripe_img{margin: 25px auto;}
  button[type='submit']{border-radius:0; padding: 5px; font-size: 12px;}
  </style>
  <div class="main_wrap-[!layout_style!]">
  <article class="form_wrap">
    <div class="form_title">
      <h3>Current Card</h3>
      <h3>****[!current_card_last4!]</h3>
    </div>
    <form action="/change_card/" id="payment-form" method="post">
      <span class="payment-errors"></span>
      <span class="payment-errors" ng-show="program_status=='Active'&&stripe_cus_id&&stripe_subscription_id">You have already enrolled in a program.</span>
    <table>  
      <tr>
        <td class="label">Card Number*</td>
        <td class="input"><input type="text" size="20" data-stripe="number"/></td>
      </tr>
      <tr>
        <td class="label">CVC*</td>
        <td class="input"><input type="text" size="4" data-stripe="cvc"/></td>
      </tr>
      <tr>
        <td class="label">Expiration (MM/YYYY)*</td>
        <td class="input">
          <input type="text" size="2" data-stripe="exp-month"/>
          <span> / </span>
          <input type="text" size="4" data-stripe="exp-year"/>
        </td>
      </tr>
      <tr>
        <td></td>
        <td style="text-align:right"><button type="submit" ng-disabled="program_status=='Active'&&stripe_cus_id&&stripe_subscription_id">Change Card</button></td>
      </tr>
     </table>
    </form>
    <img class="stripe_img" style="width:200px;" src='/pics/stripe.png'>
  </article><!-- - /form_wrap - -->
  </div><!-- .main_wrap -->
'''



payment_page_html = '''
  <style>
  body { background: url("../../pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }
.content_wrap { background-color: rgba(0,0,0, 0.6); color: #fff; text-align: center; padding: 20px; padding-bottom: 5px; width: 425px; margin: 0 auto; border: 1px solid white; }
.content_wrap span { font-size: 24px; }
  table { width: 100%; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; width: 75px; }
  td.input { font-size: 14px; text-align: left; padding-left: 10px; width: 175px; }
  input[name="client_name"],input[name="client_phone"],input[name="cc_number"]{ width: 225px; height: 16px; }
  textarea { width: 225px; height: 50px; }
  .form_title{ background-color: rgba(0,0,0, 0.5); padding: 5px 0; color:#fff; text-align:center; width: 100%; margin-bottom: 25px; border: 1px solid #999; }
  .payment-errors{ border: 1px solid red; font-size: 14px; padding: 10px; content: white; margin-bottom: 15px; }
  table.card_info { border-top: 1px solid #81C784; padding-top: 25px; margin-top: 25px; }
  .stripe_img{ margin: 25px auto; text-align: center; border-top: 1px solid #81C784; padding-top: 25px; margin-bottom: 45px; }
  .submit_button_wrap { margin-top: 25px; }
  button[type='submit']{ border-radius: 3px; padding: 10px; font-size: 12px; }
  </style>
  <div class="main_wrap-[!layout_style!]">
  <article class="content_wrap">
    <div class="form_title">
      <h3>[!program_chosen!] Program</h3>
      <h3>Price: $[!price!]/month</h3>
    </div>
    <form action="/charge_card/" id="payment-form" method="post">
      <div class="payment-errors_wrap"></div>
      <span class="payment-errors" ng-show="program_status=='Active'&&stripe_cus_id&&stripe_subscription_id">You have already enrolled in a program.</span>
    <table class="address_info">
      <tr>
        <td class="label">Name*</td>
        <td class="input"><input type="text" name="client_name" required/></td>
      </tr>
      <tr class="hide">
        <td class="label">Email*</td>
        <td class="input"><input type="text" name="client_email" ng-model="client_email" required/></td>
      </tr>
      <tr class="hide">
        <td class="label">Program*</td>
        <td class="input"><input type="text" name="client_program" ng-model="program_chosen" required/></td>
      </tr>
      <tr class="hide">
        <td class="label">Price*</td>
        <td class="input"><input type="text" name="amout" ng-model="price" required/></td>
      </tr>     
      <tr>
        <td class="label">Phone</td>
        <td class="input"><input type="text" name="client_phone" /></td>
      </tr>   
      <tr>
        <td class="label">Address</td>
        <td class="input"><textarea type="text" name="client_address"></textarea></td>
      </tr>
    </table>
    <table class="card_info">
      <tr>
        <td class="label">Card Number*</td>
        <td class="input"><input type="text" name="cc_number" size="20" data-stripe="number"/></td>
      </tr>
      <tr>
        <td class="label">CVC*</td>
        <td class="input"><input type="text" size="4" data-stripe="cvc"/></td>
      </tr>
      <tr>
        <td class="label">Expiration (MM/YYYY)*</td>
        <td class="input">
          <input type="text" size="2" data-stripe="exp-month"/>
          <span> / </span>
          <input type="text" size="4" data-stripe="exp-year"/>
        </td>
      </tr>
     </table>
      <div class="submit_button_wrap">
        <button type="submit" ng-disabled="program_status=='Active'&&stripe_cus_id&&stripe_subscription_id">Subscribe to Program</button></div>
    </form>
    <div class="stripe_img"><img style="width:150px;" src='/pics/stripe.png'></div>
  </article><!-- - /form_wrap - -->
  </div><!-- . main_wrap -->
'''


payment_success_page_html = '''
  <div class="main_wrap-[!layout_style!]">
  <h2>Thank you for your payment.</h2>
  <h2>You will recieve an email reciept.</h2>
  </div><!-- . main_wrap -->
'''

cancel_program_success_page_html = '''
  <div class="main_wrap-[!layout_style!]">
  <h2>Your have quit the program.</h2>
  </div><!-- . main_wrap -->
'''





