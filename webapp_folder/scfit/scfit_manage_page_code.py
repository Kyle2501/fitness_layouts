# -*- coding: latin-1 -*-
# - HTML Page Code


admin_nav_html = '''
  <nav class="main_nav"><ul>
    <a href="../../"><li id="programsNav">&#8672; Public</li></a>
    <a href="../../manage"><li id="manage_pageNav">Manage Page</li></a>
    <a href="../../manage/videos"><li id="manage_videosNav">Manage Videos</li></a>
    <a href="../../manage/exercise"><li id="manage_exerciseNav">Manage Library</li></a>
    <a href="../../manage/client"><li id="manage_clientsNav">Manage Clients</li></a>
    <a href="../../manage/waitlist"><li id="manage_waitlistNav">Manage Waitlist</li></a>
    <a href="../../manage/template"><li id="manage_templatesNav">Manage Templates</li></a>
    <a href="../../manage/pg_workout"><li id="manage_pg_workoutNav">P/G Workout</li></a>
    <a href="../../manage/sb_workout"><li id="manage_sb_workoutNav">S/B Workout</li></a>
    <a href="../../manage/testimonial"><li id="testimonialNav">Testimonial</li></a>
  </ul></nav><!-- - /main_nav - -->
'''




manage_page_html = '''<style>
body { background: url("../../pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }

header { background: rgba(0,0,0, 0.6); color: #fff; }

.main_wrap-desktop { padding-bottom: 175px; max-width: 650px; }
.option_wrap { background-color: rgba(0,0,0,0.4); }


</style>
  <div class="main_wrap-[!layout_style!]">
    <div class="option_wrap">
      <a href="/">View Public Site</a>
      <a href="/"><button>Open</button></a>
    </div>
    
    <div class="option_wrap">
      <a href="../../manage/bikini_bootcamp">Manage Bikini Bootcamp</a>
      <a href="../../manage/bikini_bootcamp"><button>Open</button></a>
    </div>
    <div class="option_wrap">
      <a href="../../manage/weekly_video">Manage Weekly Video</a>
      <a href="../../manage/weekly_video"><button>Open</button></a>
    </div>
    <div class="option_wrap">
      <a href="../../manage/homepage_video">Manage Homepage Video</a>
      <a href="../../manage/homepage_video"><button>Open</button></a>
    </div>
    <div class="option_wrap">
      <a href="../../manage/client">Manage Clients</a>
      <a href="../../manage/client"><button>Open</button></a>
    </div>
    <div class="option_wrap">
      <a href="../../manage/exercise">Manage Exercise Liberary</a>
      <a href="../../manage/exercise"><button>Open</button></a>
    </div>
 
    <div class="option_wrap">
      <a href="../../manage/pg_workout">Platinum &amp; Gold Workouts</a>
      <a href="../../manage/pg_workout"><button>Open</button></a>
    </div>
    <div class="option_wrap">
      <a href="../../manage/sb_workout">Silver &amp; Bronze Workouts</a>
      <a href="../../manage/sb_workout"><button>Open</button></a>
    </div>
    <div class="option_wrap">
      <a href="../../manage/template">Manage Workout Templates</a>
      <a href="../../manage/template"><button>Open</button></a>
    </div>
    <div class="option_wrap">
      <a href="../../manage/testimonial">Manage Testimonials</a>
      <a href="../../manage/testimonial"><button>Open</button></a>
    </div>
    <div class="option_wrap">
      <a href="../../manage/waitlist">Manage Waitlist</a>
      <a href="../../manage/waitlist"><button>Open</button></a>
    </div>

  </div><!-- .main_wrap -->
'''


manage_videos_page_html = '''


Manage Videos

'''


manage_weekly_video_page_html = '''<style type="text/css">
pre { white-space: pre-wrap; white-space: -moz-pre-wrap; white-space: -pre-wrap;  white-space: -o-pre-wrap; word-wrap: break-word; }
.testimonial_wrap { border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px; }


.item_wrap { display: inline-block; width: 100%; }
.item_data { position: relative; margin: 5px; padding: 5px; border: 1px solid grey; border-radius: 3px; height: 195px; }
.item_name { }
.item_icon { overflow: hidden; outline: 1px solid #eee; position: absolute; top: 35px; left: 15px; width: 125px; bottom: 25px; }
.icon_data { overflow: hidden; }
.icon_data img { width: 100%; }
.item_text { position: absolute; outline: 1px solid #eee; right: 20px; width: 140px; padding: 10px; top: 10px; bottom: 75px; font-size: 12px; }
.item_date { position: absolute; bottom: 5px; left: 5px; font-size: 12px; }
.item_buttons { position: absolute; right: 15px; bottom: 5px; text-align: right; }
    
    

.show_btn { color: steelblue; }
.testimonial_thumb { max-width: 100px; }
.modal-backdrop { position: fixed; top: 0; left: 0; bottom: 0; right: 0;  z-index: 150;  background:rgba(0,0,0, 0.6); }
.modal { position: absolute; top: 25px; z-index: 200; text-align: center; margin: auto auto; max-height: 90%; max-width: 90%; }
#lg_img { max-height: 600px; max-width: 800px; margin: auto auto; }


@media screen and (min-width: 550px) {
.list_wrap { margin: 0 auto; width: 450px; }
}

@media screen and (min-width: 750px) {
.item_wrap { width: 50%; }
.list_wrap { width: 750px; }
}

@media screen and (min-width: 900px) {
.list_wrap { width: 850px; }
}

</style>
  <div class="main_wrap-[!layout_style!]">
  
  <div class="list_wrap">
  
    <a href='/publish/weekly_video'><button>Add A New Weekly Video</button></a>
    <hr>

    <div class="modal-backdrop" ng-show="modal_show"></div>
    <div class="modal" ng-show="modal_show">
      <img id="lg_img" ng-src='[!lg_img_url!]'>
      <button ng-click="hide_lg_img()">Close</button>
    </div>

    <div class="item_wrap" ng-repeat="item in weekly_video_data | orderBy: '-add_time'">
        <div class="item_data">
          <div class="item_name">[!item.video_name!]</div>
          <div class="item_icon"><div class="icon_data">
            <img ng-src="/render_img?weekly_video?thumb?[!item.data_id!]">
          </div></div>
          <div class="item_text">[!item.video_text!]</div>
          <div class="item_date">added on [!item.video_date!]</div>
          <div class="item_buttons">
            <button ng-click="delete(item.data_id)">Remove</button>
            &nbsp;
            <a ng-href='/edit/weekly_video?[!item.data_id!]'><button>Edit Info</button></a>
            <br />
            <button ng-click="setCurrent(item.data_id)">set Current</button>
          </div><!-- . item_buttons - -->
        </div><!-- . item_data - -->
      </div><!-- . item_wrap -->
     </div><!-- . list_wrap - -->

  </div><!-- . main_wrap - -->
'''


publish_weekly_video_page_html = '''<style>
.main_wrap-desktop { padding-top: 30px; }
.form_wrap { margin: 0 auto; width: 425px; position: relative; }
.form_wrap table { margin-bottom: 25px; }
tr { height: 32px; }
td.label { text-align: right; padding-right: 10px; }
td.input input { width: 100%; height: 20px; }
td.input textarea { width: 100%; height: 45px; }
.form_wrap footer { position: absolute; bottom: 0; right: 0; padding: 10px; }
</style>
  <div class="main_wrap-[!layout_style!]">
    <header class="hi"><span class="color_b">
      <span ng-show="!if_edit">Publish</span>
      <span ng-show="if_edit">Edit</span>
      Video for Weekly
    </span></header>
    <article class="form_wrap">
      <form action="../../manage/add_weekly_video" enctype="multipart/form-data" method="post">
        <table>
        
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' ng-required="if_edit" /></td>
          </tr>
          
          <tr>
            <td class="label">Video Name</td>
            <td class="input"><input type="text" name="video_name" ng-model="item.video_name"/></td>
          </tr>
          
          <tr>
            <td class="label">Video Text</td>
            <td class="input"><textarea name="video_text" ng-model="item.video_text"></textarea></td>
          </tr>
          
          <tr>
            <td class="label">Image File</td>
            <td class="input"><input type="file" name="image_file"/></td>
          </tr>
        </table>
          
        <footer>
          <a href="/manage/weekly_video"><button type="button">Cancel</button></a>
          <span ng-show="!if_edit"><input type="submit" value="Add Weekly Video" /></span>
          <span ng-show="if_edit"><input type="submit" value="Save Edit" /></span>
        </footer>
        
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - -->  
'''


upload_weekly_video_page_html = '''
  <div class="main_wrap-[!layout_style!]">
    <header class="hi"><span class="color_b">Upload Video for Weekly</span></header>
    <article class="form_wrap">
      <form action="{0}" enctype="multipart/form-data" method="post">
        <table>
        
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' required/></td>
          </tr>

          <tr>
            <td class="label">Upload Video</td>
            <td class="input"><input type="file" name="video_file"/></td>
          </tr>
          
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/weekly_video"><button type="button">Cancel</button></a>
              <input type="submit" value="Upload Weekly Video" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - -->
'''







manage_bikini_bootcamp_page_html = '''
<style type="text/css">
pre { white-space: pre-wrap; white-space: -moz-pre-wrap; white-space: -pre-wrap;  white-space: -o-pre-wrap; word-wrap: break-word; }


.item_wrap { display: inline-block; width: 100%; }
.item_data { position: relative; margin: 5px; padding: 5px; border: 1px solid grey; border-radius: 3px; height: 135px; }
.item_name { }
.item_icon { outline: 1px solid #eee; position: absolute; top: 35px; left: 15px; width: 125px; bottom: 25px; }
.icon_data {  }
.item_text { position: absolute; outline: 1px solid #eee; right: 20px; width: 140px; padding: 10px; top: 10px; bottom: 45px; font-size: 12px; }
.item_date { position: absolute; bottom: 5px; left: 5px; font-size: 12px; }
.item_buttons { position: absolute; right: 15px; bottom: 5px; }


.show_btn { color: steelblue; }
.testimonial_thumb { max-width: 100px; }
.modal-backdrop { position: fixed; top: 0; left: 0; bottom: 0; right: 0;  z-index: 150;  background:rgba(0,0,0, 0.6); }
.modal { position: absolute; top: 25px; z-index: 200; text-align: center; margin: auto auto; max-height: 90%; max-width: 90%; }
#lg_img { max-height: 600px; max-width: 800px; margin: auto auto; }

@media screen and (min-width: 550px) {
.list_wrap { margin: 0 auto; width: 450px; }
}

@media screen and (min-width: 750px) {
.item_wrap { width: 50%; }
.list_wrap { width: 750px; }
}

@media screen and (min-width: 900px) {
.list_wrap { width: 850px; }
}

</style>
  <div class="main_wrap-[!layout_style!]">
    <div class="list_wrap">
      <a href='/publish/bikini_bootcamp'><button>Add A New Bikini Bootcamp Video</button></a>
      <hr>

      <div class="modal-backdrop" ng-show="modal_show"></div>
      <div class="modal" ng-show="modal_show">
        <img id="lg_img" ng-src='[!lg_img_url!]'>
        <button ng-click="hide_lg_img()">Close</button>
      </div>

      <div class="item_wrap" ng-repeat="item in bikini_bootcamp_data | orderBy: '-add_time'">
        <div class="item_data">
          <div class="item_name">[!item.video_name!]</div>
          <div class="item_icon">
            <div class="icon_data">
              <img ng-src="/render_img?bikini_bootcamp?thumb?[!item.data_id!]">
          </div></div>
          <div class="item_text">[!item.video_text!]</div>
          <div class="item_date">on [!item.add_time | limitTo: 10 !]</div>
          <div class="item_buttons">
            <button ng-click="delete(item.data_id)">Remove</button>
            &nbsp;
            <a ng-href='/edit/bikini_bootcamp?[!item.data_id!]'><button>Edit Info</button></a>
          </div><!-- . item_buttons - -->
        </div><!-- . item_data - -->
      </div><!-- . item_wrap -->
     </div><!-- . list_wrap - -->
  </div><!-- . main_wrap - -->
'''


publish_bikini_bootcamp_page_html = '''
  <div class="main_wrap-[!layout_style!]">
    <header class="hi"><span class="color_b">
      <span ng-show="!if_edit">Publish</span>
      <span ng-show="if_edit">Edit</span>
      Video for Bikini Bootcamp
    </span></header>
    <article class="form_wrap">
      <form action="../../manage/add_bikini_bootcamp" enctype="multipart/form-data" method="post">
        <table>
        
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' ng-required="if_edit" /></td>
          </tr>

          <tr>
            <td class="label">Image File</td>
            <td class="input"><input type="file" name="image_file"/></td>
          </tr>
          
          <tr>
            <td class="label">Video Text</td>
            <td class="input"><textarea name="video_text" ng-model="item.video_text"></textarea></td>
          </tr>
          
          <tr>
            <td class="label">Video Name</td>
            <td class="input"><input type="text" name="video_name" ng-model="item.video_name"/></td>
          </tr>
          
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/bikini_bootcamp"><button type="button">Cancel</button></a>
              <span ng-show="!if_edit"><input type="submit" value="Add Bikini Bootcamp" /></span>
              <span ng-show="if_edit"><input type="submit" value="Save Edit" /></span>
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - -->  
'''


upload_bikini_bootcamp_page_html = '''
  <div class="main_wrap-[!layout_style!]">
    <header class="hi"><span class="color_b">Upload Video for Bikini Bootcamp</span></header>
    <article class="form_wrap">
      <form action="{0}" enctype="multipart/form-data" method="post">
        <table>
        
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' required/></td>
          </tr>

          <tr>
            <td class="label">Upload Video</td>
            <td class="input"><input type="file" name="video_file"/></td>
          </tr>
          
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/bikini_bootcamp"><button type="button">Cancel</button></a>
              <input type="submit" value="Upload Bikini Bootcamp" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - -->  
'''







edit_homepage_video_page_html = '''
  <style>
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td img{max-width:70px;}
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap-[!layout_style!]">
   <header class="hi" ng-show="!if_edit"><span class="color_b">Add New Exercise</span></header>
   <header class="hi" ng-show="if_edit"><span class="color_b">Edit Exercise</span></header>
    <article class="form_wrap">
      <form name="exercise_form" action="../../manage/add_exercise" enctype="multipart/form-data" method="post">
        <table>
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' ng-required="if_edit" /></td>
          </tr>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="exercise_name" ng-model='exercise_name' required/></td>
          </tr>
          <tr>
            <td class="label">Difficulty Level*</td>
            <td class="input">
              <select name="difficulty_level" ng-model='difficulty_level' required>
                <option ng-repeat='level in difficulty_levels' value="[!level.name!]">[!level.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Equipment Type*</td>
            <td class="input">
              <select name="equipment_type" ng-model='equipment_type' required>
                <option ng-repeat='equipment in equipments' value="[!equipment.name!]">[!equipment.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Muscle Targeted*</td>
            <td class="input">
              <label ng-repeat="muscle in muscles">
                <input type="checkbox" name="muscle_targeted" value="[!muscle.name!]" ng-model="muscle.selected" ng-click="toggle_selection()" ng-required="!if_any_selected"> [!muscle.name!]<br>
              </label>            
            </td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><img ng-src="/render_img?exercise?thumb?[!data_id!]"></td>
          </tr>
          <tr>
            <td class="label"></td>
            <td class="input"><input type="file" name="exercise_photo"/></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/exercise"><button type="button">Cancel</button></a>
              <input type="submit" ng-disabled='exercise_form.$invalid' value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - -->
'''










manage_homepage_video_page_html = '''
  <style type="text/css">
    pre { white-space: pre-wrap; white-space: -moz-pre-wrap; white-space: -pre-wrap;  white-space: -o-pre-wrap; word-wrap: break-word; }
    .testimonial_wrap { border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px; }
    .show_btn { color: steelblue; }
    .testimonial_thumb { max-width: 100px; }
    .modal-backdrop { position: fixed; top: 0; left: 0; bottom: 0; right: 0;  z-index: 150;  background:rgba(0,0,0, 0.6); }
    .modal { position: absolute; top: 25px; z-index: 200; text-align: center; margin: auto auto; max-height: 90%; max-width: 90%; }
    #lg_img { max-height: 600px; max-width: 800px; margin: auto auto; }
  </style>
  <div class="main_wrap-[!layout_style!]">
    <a href='/publish/homepage_video'><button>Add A New Homepage Video</button></a>
    <hr>

    <div class="modal-backdrop" ng-show="modal_show"></div>
    <div class="modal" ng-show="modal_show">
      <img id="lg_img" ng-src='[!lg_img_url!]'>
      <button ng-click="hide_lg_img()">Close</button>
    </div>

    <div class="testimonial_wrap" ng-repeat="item in homepage_video_data | orderBy: '-add_time'">
      [!item.video_name!]<br />
      [!item.video_text!]<br />
      on [!item.add_time | limitTo: 10 !]<br />
      <br>
      <a ng-href='/edit/homepage_video?[!item.data_id!]'><button>Edit Info</button></a>
      <button ng-click="delete(item.data_id)">Remove</button>
    </div><!-- . testimonial_wrap -->

  </div><!-- . main_wrap - -->
'''


publish_homepage_video_page_html = '''
  <div class="main_wrap-[!layout_style!]">
    <header class="hi"><span class="color_b">
      <span ng-show="!if_edit">Publish</span>
      <span ng-show="if_edit">Edit</span>
      Video for Homepage
    </span></header>
    <article class="form_wrap">
      <form action="../../manage/add_homepage_video" enctype="multipart/form-data" method="post">
        <table>
        
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' ng-required="if_edit" /></td>
          </tr>

          <tr>
            <td class="label">Image File</td>
            <td class="input"><input type="file" name="image_file"/></td>
          </tr>
          
          <tr>
            <td class="label">Video Text</td>
            <td class="input"><textarea name="video_text" ng-model="item.video_text"></textarea></td>
          </tr>
          
          <tr>
            <td class="label">Video Name</td>
            <td class="input"><input type="text" name="video_name" ng-model="item.video_name"/></td>
          </tr>
          
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/homepage_video"><button type="button">Cancel</button></a>
              <span ng-show="!if_edit"><input type="submit" value="Add Homepage Video" /></span>
              <span ng-show="if_edit"><input type="submit" value="Save Edit" /></span>
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - -->  
'''


upload_homepage_video_page_html = '''
  <div class="main_wrap-[!layout_style!]">
    <header class="hi"><span class="color_b">Upload Video for Homepage</span></header>
    <article class="form_wrap">
      <form action="{0}" enctype="multipart/form-data" method="post">
        <table>
        
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' required/></td>
          </tr>

          <tr>
            <td class="label">Upload Video</td>
            <td class="input"><input type="file" name="video_file"/></td>
          </tr>
          
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/homepage_video"><button type="button">Cancel</button></a>
              <input type="submit" value="Upload Homepage Video" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - -->  
'''




edit_homepage_video_page_html = '''
  <style>
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td img{max-width:70px;}
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap-[!layout_style!]">
   <header class="hi" ng-show="!if_edit"><span class="color_b">Add New Exercise</span></header>
   <header class="hi" ng-show="if_edit"><span class="color_b">Edit Exercise</span></header>
    <article class="form_wrap">
      <form name="exercise_form" action="../../manage/add_exercise" enctype="multipart/form-data" method="post">
        <table>
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' ng-required="if_edit" /></td>
          </tr>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="exercise_name" ng-model='exercise_name' required/></td>
          </tr>
          <tr>
            <td class="label">Difficulty Level*</td>
            <td class="input">
              <select name="difficulty_level" ng-model='difficulty_level' required>
                <option ng-repeat='level in difficulty_levels' value="[!level.name!]">[!level.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Equipment Type*</td>
            <td class="input">
              <select name="equipment_type" ng-model='equipment_type' required>
                <option ng-repeat='equipment in equipments' value="[!equipment.name!]">[!equipment.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Muscle Targeted*</td>
            <td class="input">
              <label ng-repeat="muscle in muscles">
                <input type="checkbox" name="muscle_targeted" value="[!muscle.name!]" ng-model="muscle.selected" ng-click="toggle_selection()" ng-required="!if_any_selected"> [!muscle.name!]<br>
              </label>            
            </td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><img ng-src="/render_img?exercise?thumb?[!data_id!]"></td>
          </tr>
          <tr>
            <td class="label"></td>
            <td class="input"><input type="file" name="exercise_photo"/></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/exercise"><button type="button">Cancel</button></a>
              <input type="submit" ng-disabled='exercise_form.$invalid' value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - -->
'''





manage_client_page_html = '''
  <style type="text/css">

header { background:rgba(0,0,0, 0.6); color: #fff; }
  .client_wrap { display: inline-block; margin: 10px; vertical-align: top; }
    .client_data { border: 1px solid grey; text-align: left; padding: 10px; margin: 15px auto 0 auto; width: 350px;}
    .img_wrap { width: 75px; height: 75px; margin: 0 auto; margin-bottom: 15px; }
    .img_data { border: 1px solid #aaa; overflow: hidden; width: 75px; height: 75px; }
    .text_wrap { color: #333; margin-top: 5px; margin-bottom: 10px; }
    .text_wrap div { margin-bottom: 5px; font-size: 14px; letter-spacing: .08em; }
    .text_wrap span { color: red; }
    .text_wrap label { color: #888; text-align: right; width: 125px; display: inline-block; font-size: 12px; }
    .client_option_buttons { text-align: center; border-top: 1px solid white; padding-top: 10px; margin-top: 15px; }
    .item_data { display: inline-block; }

.client_list_left { display: inline-block; width: 125px; outline: 1px solid #eee; min-height: 350px; }
.client_list_right { width: 800px; outline: 1px solid #eee; display: inline-block; vertical-align: top; }
  </style>
  <div class="main_wrap-[!layout_style!]">
    <div class="page_button_wrap">
      <a href='/publish/client'><button>Add A New Client</button></a>
      <hr>
      <div class="input-group">
        
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
          &nbsp;&nbsp;
          <span>Seach:</span>
        <input ng-model='select_client' type="text">
        </p>
      </div><!-- . input-group -->
    </div><!-- . page_button_wrap - -->
<div class="client_list_left">1
  
</div><!-- . client_list_left - -->
<div class="client_list_right">
    <div class="client_wrap"
     ng-repeat="item in client_data  | orderBy: sortBy | filter: select_client ">
      <div class="client_data">
        <div class="img_wrap"><div class="img_data">
          <img ng-src="[! item.has_photo?'/render_img?client?thumb?'+item.client_email : '' !]"></div></div><!-- . img_wrap -->
        <div class="text_wrap">

        <div class="client_name">
            <label>Client Name</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.client_name !]</div>
          </div><!-- . client_name - -->

          <div class="client_email">
            <label>Client Email</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.client_email !]</div>
          </div><!-- . client_email - -->

          <div class="client_program">
            <label>Client Program</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.client_program !]</div>
          </div><!-- . client_program - -->

          <div class="program_status">
            <label>Program Status</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.program_status !]</div>
          </div><!-- . program_status - -->

        </div><!-- . text_wrap-->

        <div class="client_option_buttons">
          <button ng-click="delete(item.client_email)" ng-disabled="btn_disable">Remove</button>
          &nbsp; &nbsp;
          <a ng-href='/edit/client?[!item.client_email!]'>
            <button ng-disabled="btn_disable">Edit Info</button>
          </a>
          &nbsp; &nbsp;
          <a ng-href='/view/client?[!item.client_email!]'>
            <button ng-disabled="btn_disable">View</button>
          </a>
        </div><!-- . client_option_buttons - -->
      </div><!-- . client_data -->
    </div><!-- . client_wrap - -->
    </div><!-- . client_list_right - -->
  </div><!-- . main_wrap -->
'''

view_client_page_html = '''
  <style>
  body { background: url("../../pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }

header { background:rgba(0,0,0, 0.6); color: #fff; }
    .client_data { border: 1px solid grey; text-align: left; padding: 10px; margin: 15px auto 0 auto; width: 425px;}
    .img_wrap { text-align: center; margin: 15px; }
    .text_wrap { color: #333; margin-top: 5px; margin-bottom: 10px; }
    .text_wrap div { margin-bottom: 5px; font-size: 14px; letter-spacing: .08em; }
    .text_wrap span { color: red; }
    .text_wrap label { color: #888; text-align: right; width: 125px; display: inline-block; font-size: 12px; }
    .client_option_buttons { text-align: center; border-top: 1px solid white; padding-top: 10px; margin-top: 15px; }
    .item_data { display: inline-block; }
  </style>
  <div class="main_wrap-[!layout_style!]">
   <header class="hi"><span class="color_b">View Client [!item.client_email!]<span></header>
    <div class="client_data">
        <div class="img_wrap">
          <img ng-src="[! item.has_photo?'/render_img?client?thumb?'+item.client_email : '' !]">
        </div><!-- . img_wrap -->
        <div class="text_wrap">

        <div class="client_name">
            <label>Client Name</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.client_name !]</div>
          </div><!-- . client_name - -->

          <div class="client_email">
            <label>Client Email</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.client_email !]</div>
          </div><!-- . client_email - -->

          <div class="client_phone">
            <label>Client Phone</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.client_phone !]</div>
          </div><!-- . client_phone - -->

          <div class="client_address">
            <label>Client Address</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.client_address !]</div>
          </div><!-- . client_address - -->

          <div class="add_date">
            <label>Add Date</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.add_time | limitTo: 10 !]</div>
          </div><!-- . add_date - -->

          <div class="client_program">
            <label>Client Program</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.client_program !]</div>
          </div><!-- . client_program - -->

          <div class="program_status">
            <label>Program Status</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.program_status !]</div>
          </div><!-- . program_status - -->

          <div class="stripe_cus_id">
            <label>CID ( Stripe )</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.stripe_cus_id !]</div>
          </div><!-- . stripe_cus_id - -->

          <div class="stripe_subscription_id">
            <label>SID ( Stripe )</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.stripe_subscription_id !]</div>
          </div><!-- . stripe_subscription_id - -->

        </div><!-- . text_wrap-->

        <div class="client_option_buttons">
        
          <a ng-href='/edit/client?[!item.client_email!]'>
            <button ng-disabled="btn_disable">Edit Info</button>
          </a>

        </div><!-- . client_option_buttons - -->
      </div><!-- . client_data -->
  </div><!-- - . main_wrap - -->
'''

publish_client_page_html = '''
  <style>
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap-[!layout_style!]">
    <header class="hi"><span class="color_b">Add New Client</span></header>
   <article class="form_wrap">
      <form action="../../manage/add_client" enctype="multipart/form-data" method="post">
        <table>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" ng-model='client_name' required/></td>
          </tr>
          <tr>
            <td class="label">Email*</td>
            <td class="input"><input type="email" name="client_email" ng-model='client_email' required/></td>
          </tr>
          <tr>
            <td class="label">Client Program*</td>
            <td class="input">
              <select name="client_program" required>
                <option ng-repeat="program in programs" value="[!program.name!]">[!program.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Program Status*</td>
            <td class="input">
              <select name="program_status" required>
                <option ng-repeat="status in program_status_list" value="[!status!]">[!status!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Phone</td>
            <td class="input"><input type="text" name="client_phone" ng-model='client_phone'/></td>
          </tr>
          <tr>
            <td class="label">Address</td>
            <td class="input"><input type="text" name="client_address" ng-model='client_address'/></td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><input type="file" name="client_photo"/></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/client"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - --> 
'''

edit_client_page_html = '''
  <style>
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td img{max-width:70px;}
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap-[!layout_style!]">
   <header class="hi"><span class="color_b">Edit Client [!item.client_email!]<span></header>
    <article class="form_wrap">
      <form action="../../manage/add_client" enctype="multipart/form-data" method="post">
        <table>
          <tr class="hide">
            <td class="label">Email</td>
            <td class="input"><input type="email" name="client_email" ng-model='item.client_email' required/></td>
          </tr>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" ng-model='item.client_name' required/></td>
          </tr>
          <tr>
            <td class="label">Client Program*</td>
            <td class="input">
              <select ng-model='item.client_program' name="client_program" required>
                <option ng-repeat="program in programs" value="[!program.name!]">[!program.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Program Status*</td>
            <td class="input">
              <select ng-model='item.program_status' name="program_status" required>
                <option ng-repeat="status in program_status_list" value="[!status!]">[!status!]</option>
              </select>
            </td>
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
          <tr>
            <td class="label"><img ng-src="[! item.has_photo?'/render_img?client?thumb?'+item.client_email : '' !]"></td>
            <td class="input"></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/client"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - -->
'''






manage_exercise_page_html = '''
  <style type="text/css">
    #exercise_wrap { width: 100%; }
    #initial_category_wrap, .select_category_wrap, .select_data_wrap{width: 20%; display: inline-block; vertical-align: top; margin: 15px 5px; padding-left: 5px; padding-right: 5px; } 
    .select_category_wrap { border: 1px solid grey; }
    .select_data_wrap { width: 73%; }
    .exercise_data{border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-bottom: 15px; }
    .img_wrap { width: 15%; margin-top: 5px; }
    .img_wrap img { max-width: 100px; vertical-align: middle; }
    .text_wrap { width: 75%; }
    .text_wrap p { font-size: 12px; margin: 5px auto; }
    .img_wrap, .text_wrap { display: inline-block; vertical-align: top; }
    .blue { font-size: 14px; color: steelblue; }
    @media screen and (max-width: 800px){
      #initial_category_wrap, .select_category_wrap, .select_data_wrap { width: 95%; margin: auto; }
      .img_wrap { width: 30%; }
      .text_wrap { width: 63%; }
    }
  </style>
  <div class="main_wrap-[!layout_style!]">
    <a href='/publish/exercise'><button>Add A New Exercise</button></a>
    <hr>
    <div class="input-group">
      <p>
        Sort by: 
        <select  ng-model="sortBy" ng-init="sortBy = 'exercise_name' ">
            <option value="exercise_name" ng-selected>Exercise Name(&#8593;)</option>
            <option value="-exercise_name">Exercise Name(&#8595;)</option>
            <option value="equipment_type">Equipment Type(&#8593;)</option>
            <option value="-equipment_type">Equipment Type(&#8595;)</option>
            <option value="add_time">Add Time(&#8593;)</option>
            <option value="-add_time">Add Time(&#8595;)</option>
        </select>
      </p>
    </div><!-- .input-group -->

  <div id="exercise_wrap">
    <div class="select_category_wrap">

      <form ng-submit='sel_by_name()'>
        <label>Seach by Name:</label><br>
        <input type="text" placeholder="e.g. Push Ups" ng-model='select_name' ng-change='sel_by_name()'>
        <input class="hide" type="submit" value="Submit" />
      </form>

      <div class="show_more" ng-show="hide_more_fliters">
        <hr>
        <p ng-click='hide_more_fliters=false;'><b>More Filters <i class="fa fa-chevron-down" aria-hidden="true"></i></b></p>
      </div> <!-- . show_more -->

      <div class="muscle_targeted_filter" ng-show="!hide_more_fliters">
        <hr>
        <p><b>Muscle Targeted</b></p>
        <label>
          <input type="checkbox" name="select_all" value="all" ng-click="select_all_muscles()" class="hide"> Select All<br>        
        </label> 
        <label>
          <input type="checkbox" name="deselect_all" value="deselect_all" ng-click="deselect_all_muscles()" class="hide"> Deselect All<br>        
        </label>  
        <label ng-repeat="muscle in muscles">
          <input type="checkbox" value="[!muscle.name!]" ng-model="muscle.selected" ng-click="toggle_muscle_selection(muscle.name)"> [!muscle.name!]<br>   
        </label> 
      </div> <!-- . muscle_targeted_filter -->

      <div class="equipment_type_filter" ng-show="!hide_more_fliters">
        <hr>
        <p><b>Equipment Type</b></p> 
        <label>
          <input type="checkbox" name="select_all" value="all" ng-click="select_all_equipments()" class="hide"> Select All<br>        
        </label> 
        <label>
          <input type="checkbox" name="deselect_all" value="deselect_all" ng-click="deselect_all_equipments()" class="hide"> Deselect All<br>        
        </label>  
        <label ng-repeat="equipment in equipments">
          <input type="checkbox" value="[!equipment.name!]" ng-model="equipment.selected" ng-click="toggle_equipment_selection(equipment.name)"> [!equipment.name!]<br>   
        </label> 
      </div><!-- . equipment_type_filter --> 
      
      <div class="difficulty_level_filter" ng-show="!hide_more_fliters">
        <hr>
        <p><b>Difficulty Level</b></p> 
        <label>
          <input type="checkbox" name="select_all" ng-click="select_all_levels()" class="hide"> Select All<br>        
        </label> 
        <label>
          <input type="checkbox" name="deselect_all" ng-click="deselect_all_levels()" class="hide"> Deselect All<br>        
        </label>  
        <label ng-repeat="level in difficulty_levels">
          <input type="checkbox" value="[!level.name!]" ng-model="level.selected" ng-click="toggle_level_selection(level.name)"> [!level.name!]<br>   
        </label> 
      </div><!-- . difficulty_level_filter --> 

      <div class="show_less" ng-show="!hide_more_fliters&&small_window">
        <hr>
        <p ng-click='hide_more_fliters=true;'><b>Less Filters <i class="fa fa-chevron-up" aria-hidden="true"></i></b></p>
      </div>  <!-- . show_less --> 
    </div><!-- . select_category_wrap-->

    <div class="select_data_wrap">
      <p>Find [! (display_data| filter: select_name).length!] exercise(s)</p>
      <hr>
      <div class="exercise_data" ng-repeat="item in display_data | orderBy: sortBy | filter:select_name">
        <div class="text_wrap">
          <p>  <span class="blue">[! item.exercise_name !]</span> </p>  
          <p> Level: <span class="blue">[! item.difficulty_level !] </span></p>
          <p> Equipment Type:<span class="blue">  [! item.equipment_type !]</span> </p> 
          <p> Muscle Targeted: <span class="blue"> [! item.muscle_targeted !]</span> </p> 
          <p> Add Time: <span class="blue"> [! item.add_time | limitTo: 10 !]</span> </p>
          <p> User:<span class="blue"> [! item.user_name !]</span> </p>
          <p ng-show='item.exercise_video_key'> <a ng-href="/view_video/[!item.exercise_video_key!]" target="_blank"> View Video </a></p>
        </div><!-- . text_wrap-->

        <div class="img_wrap">
          <img ng-src="/render_img?exercise?thumb?[!item.data_id!]">
        </div><!-- . img_wrap-->

        <br>
        <a ng-href='/edit/exercise?[!item.data_id!]'><button>Edit Info</button></a>
        <a ng-href='/publish/exercise_video?[!item.data_id!]'><button>Edit Video</button></a>
        <button ng-click="delete(item.data_id)">Delete</button>
      </div><!-- . exercise_data-->
    </div><!-- . select_data_wrap-->
  </div><!-- . exercise_wrap-->
  </div><!-- . main_wrap -->
'''


publish_exercise_video_page_html = '''
  <div class="main_wrap-[!layout_style!]">
    <header class="hi"><span class="color_b">Video for [!exercise_name!]</span></header>
    <article class="form_wrap">
      <form action="{0}" enctype="multipart/form-data" method="post">
        <table>
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' required/></td>
          </tr>
          <tr>
            <td class="label">Upload Video</td>
            <td class="input"><input type="file" name="video_file"/></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/exercise"><button type="button">Cancel</button></a>
              <input type="submit" value="Add Exercise Video" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - -->  
'''


edit_exercise_page_html = '''
  <style>
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td img{max-width:70px;}
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap-[!layout_style!]">
   <header class="hi" ng-show="!if_edit"><span class="color_b">Add New Exercise</span></header>
   <header class="hi" ng-show="if_edit"><span class="color_b">Edit Exercise</span></header>
    <article class="form_wrap">
      <form name="exercise_form" action="../../manage/add_exercise" enctype="multipart/form-data" method="post">
        <table>
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' ng-required="if_edit"/></td>
          </tr>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="exercise_name" ng-model='exercise_name' required/></td>
          </tr>
          <tr>
            <td class="label">Difficulty Level*</td>
            <td class="input">
              <select name="difficulty_level" ng-model='difficulty_level' required>
                <option ng-repeat='level in difficulty_levels' value="[!level.name!]">[!level.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Equipment Type*</td>
            <td class="input">
              <select name="equipment_type" ng-model='equipment_type' required>
                <option ng-repeat='equipment in equipments' value="[!equipment.name!]">[!equipment.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Muscle Targeted*</td>
            <td class="input">
              <label ng-repeat="muscle in muscles">
                <input type="checkbox" name="muscle_targeted" value="[!muscle.name!]" ng-model="muscle.selected" ng-click="toggle_selection()" ng-required="!if_any_selected"> [!muscle.name!]<br>
              </label>            
            </td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><img ng-src="/render_img?exercise?thumb?[!data_id!]"></td>
          </tr>
          <tr>
            <td class="label"></td>
            <td class="input"><input type="file" name="exercise_photo"/></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/exercise"><button type="button">Cancel</button></a>
              <input type="submit" ng-disabled='exercise_form.$invalid' value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - -->
'''











edit_template_page_html = '''
  <style>
  .form_wrap, .small_form_wrap{width:90%;margin:auto; }
  .small_form_wrap { padding:0; border: 1px solid #ccc; }
  tr { height: 32px; overflow-x:auto; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td.input { font-size: 14px; text-align: left; padding-left: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  .modal{ position: absolute; top: 0; z-index: 200;  padding: 25px; background: #fff; text-align: center; margin: auto; }
  .modal-backdrop{position: fixed; top: 0; left: 0; bottom: 0; right: 0;  z-index: 100;  background: rgba(0,0,0, 0.6); }
  .main_wrap a { text-decoration:underline; }
  .outter_wrap { width: 100%; overflow-x:scroll; }
  .workout_plan { width: 1200px; table-layout: fixed; }
  .workout_plan th { background:#37474F; color: #fff; padding: 5px; min-width: 100px; }
  .workout_plan td { padding: 5px; min-width: 100px; }
  .White, .Red, .Orange,.LightBlue, .LightGreen, .LightGrey, .BlueGrey { border:1px solid grey; padding: 10px 10px; margin: 5px auto; }
  .White{background:#fff;}.Red{background:#FFCDD2;}.Orange{background:#FFE0B2;}.LightBlue{background:#81D4FA;}.LightGreen{background:#B2DFDB;}.LightGrey{background:#E0E0E0;}.BlueGrey{background:#B0BEC5;}
  .btn_wrap{margin: 25px auto;}
  pre{ white-space: pre-wrap; white-space: -moz-pre-wrap; white-space: -pre-wrap;  white-space: -o-pre-wrap; word-wrap: break-word;}
  .button_wrap { border: 1px solid #bbb; border-radius: 3px; padding: 3px; font-size: 14px; width: 50px; margin: 5px; text-align: center; cursor: pointer; }
  .button_wrap:hover { border: 1px solid #555; }
  </style>

  <div class="main_wrap-[!layout_style!]">
   <header ng-show="!if_edit" class="hi"><span class="color_b">Add a New Template</span></header>
   <header ng-show="if_edit" class="hi"><span class="color_b">Edit Template [!item.template_name!]</span></header>
    <article class="form_wrap">
      <form ng-submit="save_workout_plan()" method="post">
        <table>
          <tr class="hide">
            <td class="label">Datd ID</td>
            <td class="input"><input type="text" name="client_email" ng-model='item.data_id' ng-required="if_edit" ></td>
          </tr>
          <tr>
            <td class="label">Template Name</td>
            <td class="input"><input type="text" name="template_name" ng-model='item.template_name' required/></td>
          </tr>
         

           <tr>
            <td class="label">Muscles</td>
            <td class="input"><input type="text" name="muscles" ng-model='item.muscles_array' required/></td>
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
          <a href="/manage/template"><button type="button">Cancel</button></a>
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
            <td class="label">Muscles</td>
            <td class="input"><input type="text" name="muscles" ng-model='item.muscles_array' required/></td>
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

manage_view_template_page_html = '''
  <style type="text/css">
    .main_wrap a { text-decoration: underline; }
    .outter_wrap { width: 100%; overflow-x: scroll; }
    .workout_plan { width: 1200px; table-layout: fixed; }
    .workout_plan th { background:#37474F; color: #fff; padding: 5px; min-width: 100px; }
    .workout_plan td { padding: 5px; min-width: 100px; }
    .White, .Red, .Orange, .LightBlue, .LightGreen, .LightGrey, .BlueGrey { border: 1px solid grey; }
    .White { background: #fff; }
    .Red { background: #FFCDD2; }
    .Orange { background: #FFE0B2;}
    .LightBlue { background: #81D4FA; }
    .LightGreen { background: #B2DFDB; }
    .LightGrey { background: #E0E0E0; }
    .BlueGrey { background: #B0BEC5; }
    .red {  }
    pre { white-space: pre-wrap; white-space: -moz-pre-wrap; white-space: -pre-wrap;  white-space: -o-pre-wrap; word-wrap: break-word; }
    .hi { color: #fff; }
    .list_wrap { }
    .list_data { background-color: #fff; border: 1px solid #000; min-height: 135px; position: relative; border-radius: 2px; border-left: 1px solid red; }
    .list_data:hover .pic_wrap { border: 1px solid #000; }
    .color_wrap { width: 70px; height: 8px; border: 1px solid grey; position: absolute; right: 15px; top: 10px; }
    .item_title { margin: 15px; padding-top: 10px; padding-left: 5px; margin-bottom: 5px; }
    .item_title a { color: #111; }
    .pic_wrap { width: 150px; margin: 10px; margin-left: 15px; display: inline-block; vertical-align: top; text-align: center; border: 1px solid #eee; border-radius: 5px; min-height: 125px; padding-top: 25px; margin-top: 5px; }
    .set_wrap { display: inline-block; }
    .print_options { background-color: #fff; padding: 10px; }
    .table_button { display: inline-block; cursor: pointer; margin: 15px; }
    .table_wrap { }
    .show_table-yes { display: block; }
    .show_table-no { display: none; }
  </style>
  <div class="main_wrap-[!layout_style!]">
     <header class="hi">Template [!item.template_name!]</header>
      <a ng-href='/manage/template'><button>Back</button></a>
      <a ng-href='/edit/template?[!item.data_id!]'><button>Edit Template</button></a>
      <button ng-click="delete(item.data_id)">Remove</button>

        <p>[!item.program_date!]&nbsp;&nbsp;[!item.muscles!]&nbsp;&nbsp;[!item.client_name!]</p>
        <p>[!item.general_explanation!]</p>

        <div class="outter_wrap">


          <div class="list_wrap" ng-repeat="exercise in item.workout">
            <div class="list_data">
              <div class="color_wrap" ng-class="exercise.exercise_color"></div>
              <div class="item_title">
                <a href="/exercise_detail/?data_id=[!exercise.exercise_id!]" target="_blank">
                [!exercise.name!]</a>
              </div><!-- . item_title - -->
              <a href="/exercise_detail/?data_id=[!exercise.exercise_id!]" target="_blank">
              <div class="pic_wrap">
                <img ng-src="/render_img?exercise?thumb?[!exercise.exercise_id!]">
              </div><!-- . pic_wrap - --></a>
              <div class="set_wrap">
                <pre>Warm Up - [!exercise.warmup_set!]</pre>
                <pre>Set 1 | [!exercise.set1!]</pre>
                <pre>Set 2 | [!exercise.set2!]</pre>
                <pre>Set 3 | [!exercise.set3!]</pre>
                <span ng-show="table_length>=4"><pre>Set 4 | [!exercise.set4!]</pre></span>
                <span ng-show="table_length>=5"><pre>Set 5 | [!exercise.set5!]</pre></span>
              </div><!-- . set_wrap - -->
            </div><!-- . list_data - -->
          </div><!-- . list_wrap - -->

          <div class="print_options">
            <div class="table_button" ng-click="show_table='no'">Hide Table</div>
            <div class="table_button" ng-click="show_table='yes'">Show Table</div>
          </div><!-- . print_options -->
          <div class="table_wrap show_table-[!show_table!]">
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
              </tr><!-- . exercise_list -->
            </table>
          </div><!-- . table_wrap - -->
        </div><!-- .outter_wrap -->

  </div><!-- .main_wrap -->
'''








manage_testimonial_page_html = '''
  <style type="text/css">
    pre { white-space: pre-wrap; white-space: -moz-pre-wrap; white-space: -pre-wrap;  white-space: -o-pre-wrap; word-wrap: break-word; }
    .testimonial_wrap { border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px; }
    .show_btn { color: steelblue; }
    .testimonial_thumb { max-width: 100px; }
    .modal-backdrop { position: fixed; top: 0; left: 0; bottom: 0; right: 0;  z-index: 150;  background:rgba(0,0,0, 0.6); }
    .modal{position: absolute; top:25px; z-index: 200; text-align: center; margin: auto auto; max-height:90%; max-width:90%;}
    #lg_img{max-height: 600px; max-width: 800px; margin: auto auto;}
  </style>
  <div class="main_wrap-[!layout_style!]">
    <a href='/publish/testimonial'><button>Add A New Testimonial</button></a>
    <hr>

    <div class="modal-backdrop" ng-show="modal_show"></div>
    <div class="modal" ng-show="modal_show">
      <img id="lg_img" ng-src='[!lg_img_url!]'>
      <button ng-click="hide_lg_img()">Close</button>
    </div>

    <div class="testimonial_wrap" ng-repeat="item in testimonial_data | orderBy: '-add_time'">
      <testimonial-view></testimonial-view>
      <br>
      <a ng-href='/edit/testimonial?[!item.data_id!]'><button>Edit Info</button></a>
      <button ng-click="delete(item.data_id)">Remove</button>
    </div><!-- . testimonial_wrap -->

  </div><!-- . main_wrap - -->
'''

edit_testimonial_page_html = '''
  <style>
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap-[!layout_style!]">
   <header class="hi" ng-show="!if_edit"><span class="color_b">Add New Testimonial</span></header>
   <header class="hi" ng-show="if_edit"><span class="color_b">Edit Testimonial</span></header>
   <article class="form_wrap">
      <form action="/manage/add_testimonial" enctype="multipart/form-data"  method="post">
        <table>
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' ng-required="if_edit"/></td>
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
          <tr>
            <td class="label">
             <img ng-src="[! item.has_photo?'/render_img?testimonial?thumb?'+item.data_id : '' !]">
             </td>
            <td class="input"></td>         
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/testimonial"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - . main_wrap - --> 
'''







add2waitlist_page_html = '''
  <div class="main_wrap-[!layout_style!]">
    <p>You will be added to the Waitlist for [!program_chosen!] Program ($[!price!]/month).</p>
    <article class="form_wrap">
      <form action="/manage/add_waitlist" method="post">
        <table>
          <tr>
            <td class="label">Name</td>
            <td class="input"><input type="text" name="client_name" required/></td>
          </tr>
          <tr class="hide">
            <td class="label">Program</td>
            <td class="input"><input type="text" name="client_program" ng-model='program_chosen' required/></td>
          </tr>
          <tr class="hide">
            <td class="label">Email</td>
            <td class="input"><input type="text" name="client_email" ng-model='client_email' required/></td>
          </tr>
          <tr>
            <td class="label">Phone (optional)</td>
            <td class="input"><input type="text" name="client_phone"/></td>
          </tr>
          <tr>
            <td class="label">Adress (optional)</td>
            <td class="input"><input type="text" name="client_address"/></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href='/programs'><button type='button'>Cancel</button></a>
              <input type="submit" value="Yes" /></td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- . main_wrap -->
'''






