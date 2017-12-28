# -*- coding: latin-1 -*-
# - HTML Page Code





#----------------------------------------------#
#        Exercises                             #
#----------------------------------------------#

exercises_page_html = '''
<link href="https://fonts.googleapis.com/css?family=Cousine" rel="stylesheet">
  <style type="text/css">
  body { background: url("pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }
    #exercise_wrap { width: 1000px; }
    #initial_category_wrap, .select_category_wrap, .select_data_wrap{ display: inline-block; vertical-align: top; margin: 15px 5px; } 
    .select_category_wrap { width: 175px; border-left: 1px solid #eee; border-right: 1px solid #eee; box-shadow: 0 1px 10px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24); padding: 15px; background-color: rgba(255,255,255,0.9); font-family: 'Cousine', sans-serif; }
    .select_data_wrap { width: 73%; }

    .filter_name { font-family: 'Lato', sans-serif; }
    .filter_name span { color: steelblue; font-size: 12px; cursor: pointer;  }

    .exercise_card_wrap { width: 350px; margin: 5px; display: inline-block; vertical-align: top; }
    .exercise_card_data { border: 1px solid #aaa; border-radius: 3px; text-align: left;  padding: 3px; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24); position: relative;
  transition: all 0.3s cubic-bezier(.25,.8,.25,1); background-color: white; }
    .exercise_card_data:hover { border: 1px solid #444; box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22); }
    
    .card_middle { position: relative; height: 120px; margin-top: 50px; }
    
    .card_button_wrap { text-align: right; }
    
    
    .img_wrap { text-align: center; margin-top: 5px; display: inline-block; outline: 1px solid #111; width: 100px; position: absolute; left: 0; top: 0; margin: 10px; }
    .img_wrap img { max-width: 100px; vertical-align: middle; }
    .text_wrap { padding: 10px; padding-top: 0; display: inline-block; position: absolute; right: 0; top: 0; left: 125px; }
    .text_wrap p { font-size: 12px; margin: 5px auto; }
    .blue { font-size: 14px; color: steelblue; }
    .card_name { color: black; font-size: 14px; font-weight: bold; font-family: 'Cousine', sans-serif; border-right: 1px solid #eee; border-bottom: 1px solid #eee; position: absolute; left: 0; top: 0; right: 150px; padding: 10px; }
    .difficulty_level { position: absolute; top: 10px; right: 15px; }
    
    
    .save { color: #ddd; }

.select_all_wrap { outline: 1px dotted red; margin-top: 15px; padding: 5px; }

    .button_wrap { display: inline-block; margin: 10px; border: 1px solid #aaa; border-radius: 3px; padding: 5px; width: 45px; text-align: center; cursor: pointer; font-size: 12px; font-family: 'Lato', sans-serif; background-color: white; }
    .button_wrap:hover { border: 1px solid #444; }

    .search_welcome { background-color: rgba(255,255,255,0.9); padding: 15px; color: #000; }


    .sort_wrap { display: inline-block; font-size: 14px; background-color: rgba(255,255,255,0.9); padding: 10px; padding-left: 25px; color: #000; }
    .show_more { display: inline-block; }

    .input_group { display: inline-block; margin-left: 15px; }

    form { display: inline-block; }

    .found_count { display: inline-block; float: right; }

    .muscle_targeted_filter .button_wrap { width: 50px; margin: 5px; }

    input[type="checkbox"]{ display: none; }
    span.checkbox { padding-left: 10px; border-left: 3px solid rgba(255,255,255,0.0); color: #999; margin-left: 5px; }
    span.checkbox:hover { border-left: 3px solid red; }
    input[type="checkbox"]:checked + span.checkbox { border-left: 3px solid red; color: #111; }

    .side_list_wrap label { display: block; margin-bottom: 7px; cursor: pointer; }

    .main_wrap-desktop { padding-top: 0; margin-left: 155px; }
    
    .equipment_wrap { position: absolute; left: 15px; bottom: 10px; }
    
    .text_wrap ul { margin: 0; }



    @media screen and (max-width: 650px){
      #exercise_wrap { width: 100%; margin: auto; }
      .select_category_wrap { display: block; width: 90%; font-size: 13px; text-align: right; }
      .select_data_wrap { width: 95%; }

      span.checkbox { padding-right: 10px; border-right: 3px solid rgba(255,255,255,0.0); margin-right: 5px; border-left: 0; margin-left: 0; padding-left: 0; }
      span.checkbox:hover { border-right: 3px solid red; border-left: 0; }
      input[type="checkbox"]:checked + span.checkbox { border-right: 3px solid red; border-left: 0; }

      .exercise_card_wrap { width: 100%; margin-left: 0; }
      

    }
  </style>
  <div class="main_wrap-[!layout_style!]">


  <div id="exercise_wrap">

     <div class="select_category_wrap">
       <div>Exercises: _</div>
       <div class="select_all_wrap">Select<br />
         <div class="button_wrap"><label>
          <input type="checkbox" name="deselect_all" value="deselect_all" ng-click="deselect_all_muscles()" class="hide">None<br></label></div>
         <div class="button_wrap"><label>
          <input type="checkbox" name="select_all" value="all" ng-click="select_all_muscles()"
            class="hide">All<br></label></div>
       </div><!-- . select_all_wrap - -->

    
      <div class="show_more" ng-init="more_fliters='yes'">
        <p ng-click="more_fliters='yes'" ng-show="more_fliters=='no'"><b>Show Filters &nbsp; <i class="fa fa-chevron-down" aria-hidden="true"></i></b></p>
        <p ng-click="more_fliters='no'" ng-show="more_fliters=='yes'"><b>Hide Filters &nbsp;<i class="fa fa-chevron-up" aria-hidden="true"></i></b></p>
      </div> <!-- . show_more -->

      <div class="show_less" ng-show="!hide_more_fliters&&small_window">
        <hr>
        <p ng-click='hide_more_fliters=true;'><b>Less Filters <i class="fa fa-chevron-up" aria-hidden="true"></i></b></p>
      </div>  <!-- . show_less --> 

      <div class="more_filters_wrap" ng-show="more_fliters=='yes'">

        <div class="muscle_targeted_filter" ng-init="muscle_show='yes'">
        <hr>
        <p class="filter_name"><b>Muscle Targeted</b>&nbsp;&nbsp;
          <span ng-click="muscle_show='no'" ng-show="muscle_show=='yes'">Hide</span>
          <span ng-click="muscle_show='yes'" ng-show="muscle_show=='no'">Show</span>
        </p>
        <div class="side_list_wrap" ng-show="muscle_show=='yes'">
        <label ng-repeat="muscle in muscles">
          <input type="checkbox" value="[!muscle.name!]" ng-model="muscle.selected" ng-click="toggle_muscle_selection(muscle.name)">&nbsp;<span class="checkbox">[!muscle.name!]</span><br>   
        </label>
        
        
        <div class="button_wrap"><label>
      <input type="checkbox" name="select_all" value="all" ng-click="select_all_muscles()" class="hide">All<br>        
    </label></div>

      <div class="button_wrap" ><label>
      <input type="checkbox" name="deselect_all" value="deselect_all" ng-click="deselect_all_muscles()" class="hide"> Deselect<br>        
    </label></div>
        
      </div><!-- . side_list_wrap -->

      </div> <!-- . muscle_targeted_filter -->

      <div class="difficulty_level_filter" ng-init="difficulty_show='no'">
        <hr>
        <p class="filter_name"><b>Difficulty Level</b>&nbsp;&nbsp;
          <span ng-click="difficulty_show='no'" ng-show="difficulty_show=='yes'">Hide</span>
          <span ng-click="difficulty_show='yes'" ng-show="difficulty_show=='no'">Show</span>
        </p>
        <div class="side_list_wrap" ng-show="difficulty_show=='yes'">
        <label ng-repeat="level in difficulty_levels">
          <input type="checkbox" value="[!level.name!]" ng-model="level.selected" ng-click="toggle_level_selection(level.name)">&nbsp;<span class="checkbox">[!level.name!]</span><br>   
        </label>
      </div>
      </div><!-- . difficulty_level_filter --> 

      <div class="equipment_type_filter" ng-init="equipment_show='no'">
        <hr>
        <p class="filter_name"><b>Equipment Type</b>&nbsp;&nbsp; 
          <span ng-click="equipment_show='no'" ng-show="equipment_show=='yes'">Hide</span>
          <span ng-click="equipment_show='yes'" ng-show="equipment_show=='no'">Show</span>
        </p>
        <div class="side_list_wrap" ng-show="equipment_show=='yes'">
        <label ng-repeat="equipment in equipments">
          <input type="checkbox" value="[!equipment.name!]" ng-model="equipment.selected" ng-click="toggle_equipment_selection(equipment.name)">&nbsp;<span class="checkbox"> [!equipment.name!]</span><br>   
        </label>
      </div>
      </div><!-- . equipment_type_filter --> 


    </div><!-- . /more_filters_wrap - -->
    </div><!-- . select_category_wrap-->


    <div class="select_data_wrap">
      <div class="sort_wrap">
    

    <form ng-submit='sel_by_name()'>
        <label>Seach by Name:</label> &nbsp;
        <input type="text" placeholder="e.g. Push Ups" ng-model='select_name' ng-change='sel_by_name()'>
      </form>

      <div class="input_group">
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


      <div class="found_count">
      <p style="text-align:right;">[! (display_data| filter: select_name).length!] Exercise/s Found</p>
    </div>
    </div><!-- . sort_wrap - -->
      <hr>


      <div class="exercise_card_wrap" ng-repeat="item in display_data | orderBy: sortBy | filter:select_name">
        <div class="exercise_card_data">
        
        <div class="card_name">[! item.exercise_name !]</div>
        <div class="difficulty_level">Level:&nbsp; <span class="blue">[! item.difficulty_level !] </span></div>
        
        <div class="card_middle">

          <a href="/exercise_detail/?data_id=[!item.data_id!]"><div class="img_wrap">
            <img ng-src="/render_img?exercise?thumb?[!item.data_id!]">
          </div><!-- . img_wrap--></a>

          <div class="text_wrap">  
            <p>Muscle Group:<ul><li ng-repeat="hi in item.muscle_targeted.split(',')"><span class="blue">[! hi !]</span></li></ul></p>
            
          </div><!-- . text_wrap-->
        
        </div><!-- card_middle -->
        
        <div class="equipment_wrap">Equipment:&nbsp; <span class="blue">[! item.equipment_type !]</span></div>
        
       <div class="card_button_wrap"> 
        <button class="save">Save</button>
         <a href="/exercise_detail/?data_id=[!item.data_id!]">
          <button>Detail</button>
          </a>
        </div><!-- . card_button_wrap - -->
      </div><!-- . exercise_card_data -->
      </div><!-- . exercise_card_wrap -->
    </div><!-- . select_data_wrap -->

   

  </div><!-- . exercise_wrap -->
  </div><!-- . main_wrap -->
'''





exercise_detail_page_html = '''
  <style>
 
    .detail_wrap-mobile { position: absolute; left: 0; right: 0; bottom: 85px; top: 275px; }
    .detail_wrap-desktop { margin: 15px; width: 800px; margin-left: 100px; }
    .detail_data { font-family: 'Lato', sans-serif; font-weight: 300; background-color: #000; }

    .img_wrap { text-align: center; }
    .img_wrap img { width: 100%; }

    .text_wrap { display: inline-block; vertical-align: top; }
    .detail_wrap-mobile .text_wrap {  }
    .detail_wrap-desktop .text_wrap { font-size: 16px; margin: 25px; }

    .text_wrap p { line-height: 12px; }

    .video_wrap-mobile { background-color: #444; margin: 0 auto; position: fixed; left: 0; top: 55px; right: 0; height: 275px; }
    .video_wrap-desktop { display: inline-block; width: 350px; height: 250px; margin-left: 200px; }
    .video_data { background-color: #333; padding-bottom: 20px; }

    #video_controls { position: absolute; right: 15px; }
    .video_controls:hover { opacity: 1; }
    #volume-bar { width: 50px; }
    .red_title { color: red; font-size: 18px; line-height: 34px; }
    .red { color: red; }
    .video_error { font-size: 12px; font-family: monospace; text-align: center; padding-top: 25px; color: #999; }
    .back_button a { font-size: 14px; color: #aaa; }
    .back_button a:hover { font-size: 14px; color: #333; }

    .detail_title { color: #fff; font-size: 24px; text-align: left; font-weight: bold; padding-bottom: 25px; margin-bottom: 15px; border-top: 1px solid #eee; }

    .text_wrap { color: #000; margin-top: 5px; margin-bottom: 10px; }
    .text_wrap div { margin-bottom: 5px; font-size: 14px; letter-spacing: .08em; }
    .text_wrap span { color: red; }
    .text_wrap label { color: #888; text-align: right; width: 125px; display: inline-block; font-size: 12px; }

    .item_data { display: inline-block; color: steelblue; }
    
    .back_button { position: fixed; left: 5px; bottom: 12px; z-index: 1000; }
    
    .progress_bar { display: inline-block; text-align: center; margin-right: 15px; }
    .progress_bar input { width: 100%; }
    
    .difficulty_level { position: fixed; bottom: 12px; left: 50px; z-index: 1000; }
    
    .volume_controls {  }

.control_buttons { background-color: #fff; }

    @media screen and (max-width: 800px){
      #volume-bar { width: 25px; }
    }


  </style>
  <div class="main_wrap-[!layout_style!]">


    <section class="video_wrap-[!layout_style!]">
      <div class="video_error" ng-show='!item.exercise_video_key'>No Video</div>

      <div class="video_data" ng-show='item.exercise_video_key'>
        <video id="video" width="100%" height="200" ng-src="[!video_url!]"></video>
        
      </div><!-- . video_data -->
    </section><!-- . video_wrap -->

    <div class="detail_wrap-[!layout_style!]">
      <div class="detail_data">
<div class="control_buttons">
        <div id="video_controls">
          <div class="progress_bar"><input type="range" id="seek-bar" value="0"></div>
          <button type="button" id="play-pause">Play<i class="fa fa-play"></i></button>
          
        </div><!-- . video_controls -->
        
        
         <div class="volume_controls">
 <button type="button" id="full-screen">Full Screen<i class="fa fa-expand"></i></button>
  <!-- <button type="button" id="mute">Mute<i class='fa fa-volume-off'></i></button>
   <input type="range" id="volume-bar" min="0" max="1" step="0.1" value="1"> -->
 </div>
        
      </div><!-- . control_buttons - -->

        <section class="text_wrap">
        
         <div class="detail_title">[! item.exercise_name !]</div>

        
          <div class="muscle_targeted">
            <label>Muscle Targeted</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.muscle_targeted !]</div>
          </div><!-- . muscle_targeted - -->
          <div class="equipment_type">
            <label>Equipment Type</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.equipment_type !]</div>
          </div><!-- . equipment_type - -->
          <div class="difficulty_level">
            <label>Difficulty Level</label> &nbsp; <span>|</span> &nbsp;
            <div class="item_data">[! item.difficulty_level !]</div>
          </div><!-- . difficulty_level - -->

        </section><!-- . text_wrap -->

        <section class="img_wrap"><img ng-src="[!img_url!]"></section>

      </div><!-- . detail_data -->
    </div><!-- . detail_wrap - -->
<div class="back_button"><a href="../../exercises"><button>Back</button></a></div>
  </div><!-- .main_wrap -->
'''

