# -*- coding: latin-1 -*-
# - HTML Page Code




promo_join_page_code = '''
<style>
.page_ { width: 300px; margin: 0 auto; margin-top: 75px; }


</style>
<div class="page_"><p>Promo Join</p>

<button class="sign_up_btn" ng-click=" confirm_signup('Promo') ">Sign Up</button>

</div>


'''




cam_test_page_code = '''
<style>
.page_ { margin: 75px; }



a { text-decoration: none; color: #aaa; }
a:hover { text-decoration: underline; color: #333; }

    .none { filter: none; }
    .blur { filter: blur(3px); }
    .grayscale { filter: grayscale(1); }
    .invert { filter: invert(1); }
    .sepia { filter: sepia(1); }

    button#snapshot {
      margin: 0 10px 25px 0;
      width: 110px;
    }

    .main_feed_wrap { width: 250px; padding: 8px; border: 1px solid #999; background-color: #fff; }
    video { object-fit: cover; width: 100%; }

</style>

<div class="page_">hi</div>




  <h1>Test ing Room</h1>

    <div class="top_control_wrap">
      <label for="select">Filter: </label>
      <select id="filter">
        <option value="none">None</option>
        <option value="blur">Blur</option>
        <option value="grayscale">Grayscale</option>
        <option value="invert">Invert</option>
        <option value="sepia">Sepia</option>
      </select>
      <button id="snapshot">Take snapshot</button>
      <button id="location">Get Location</button>
      <button id="test">test</button>
    </div><!-- . top_control_wrap - -->

    <div class="main_feed_wrap">
      <video autoplay></video>
      <div id="out"></div>
    </div><!-- . main_feed_wrap - -->

    <canvas></canvas>

  </div><!-- . page_wrap - -->


<script>'use strict';

var testButton = document.querySelector('button#test');
testButton.onclick = function() {
  console.log(navigator.getBattery().then());
};


var locationButton = document.querySelector('button#location');
locationButton.onclick = function() {
  var output = document.getElementById("out");

  if (!navigator.geolocation){
    output.innerHTML = "<p>Geolocation is not supported by your browser</p>";
    return;
  }

  function success(position) {
    var latitude  = position.coords.latitude;
    var longitude = position.coords.longitude;

    output.innerHTML = '<p>Latitude is ' + latitude + '° <br>Longitude is ' + longitude + '°</p>';

    var img = new Image();
    img.src = "https://maps.googleapis.com/maps/api/staticmap?center=" + latitude + "," + longitude + "&zoom=13&size=300x300&sensor=false";

    output.appendChild(img);
  };

  function error() {
    output.innerHTML = "Unable to retrieve your location";
  };

  output.innerHTML = "<p>Locating…</p>";

  navigator.geolocation.getCurrentPosition(success, error);
}; ///

var snapshotButton = document.querySelector('button#snapshot');
var filterSelect = document.querySelector('select#filter');

// Put variables in global scope to make them available to the browser console.
var video = window.video = document.querySelector('video');
var canvas = window.canvas = document.querySelector('canvas');
canvas.width = 480;
canvas.height = 360;

snapshotButton.onclick = function() {
  canvas.className = filterSelect.value;
  canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
};

filterSelect.onchange = function() {
  video.className = filterSelect.value;
};

var constraints = {
  audio: false,
  video: true
};

function handleSuccess(stream) {
  window.stream = stream; // make stream available to browser console
  video.srcObject = stream;
}

function handleError(error) {
  console.log('navigator.getUserMedia error: ', error);
}

navigator.mediaDevices.getUserMedia(constraints).
    then(handleSuccess).catch(handleError);

</script>



'''







exercises_page_html = '''
  <style type="text/css">
  .exercise_list_wrap { margin-bottom: 250px; }
  .exercise_list_data_top { width: 100%; }
    #exercise_wrap { font-family: 'Lato', sans-serif; font-weight: 300; }
    #initial_category_wrap, .select_category_wrap, .select_data_wrap { display: inline-block; vertical-align: top; margin: 15px 5px; padding-left: 5px; padding-right: 5px; } 
    .select_category_wrap { border-right: 1px solid #eee; }

    .filter_button_wrap { position: fixed; right: 5px; bottom: 130px; }

    .white { font-size: 14px; color: #fff; }
    .red { color: red; }
    .difficulty_level_filter { border-bottom: 1px solid #eee; padding: 15px; width: 350px; margin-bottom: 25px; font-size: 14px; }
    .muscle_targeted_filter { text-align: right; padding: 15px; width: 175px; }
    p.side_title { text-align: center; letter-spacing: .07em;  }
    p.top_title { letter-spacing: .07em; font-size: 16px; }
    .equipment_type_filter { text-align: right; padding: 15px; width: 175px; }
    .select_all_wrap { padding: 10px; display: inline-block; font-size: 12px; }
    .find_amount { display: inline-block; border-left: 1px solid #ccc; margin-left: 15px;  padding: 10px; padding-left: 15px; font-size: 12px; font-family: monospace; }
    
    .side_list_item { margin-bottom: 3px; cursor: pointer; display: block; font-family: 'Lato', sans-serif; font-weight: 300; }
    .open_button { position: absolute; bottom: 15px; right: 10px; }

    .main_wrap { }

    .main_wrap-mobile .select_category_wrap {  }
    .main_wrap-desktop .select_category_wrap { margin-right: 10px; }

    .main_wrap-mobile .footer_bar_wrap { display: block; }
    .main_wrap-desktop .footer_bar_wrap { display: none; }

    .filters-yes { display: inline-block }
    .filters-no { display: none; }

    .hide_filters .fa { font-size: 28px; margin: 5px; line-height: 14px; cursor: pointer; }

    .select_data_wrap { width: 380px; margin: 0 auto;  display: inline-block; }

    .item_name_list { display: inline-block; padding-top: 25px; margin-left: 15px; }

    .name_wrap { background-color: #fff; width: 405px; margin-bottom: 5px; border-left: 2px solid red; }
    .name_wrap:hover { border-left: 2px solid black; }
    .name_data { text-align: right; color: black; padding: 15px; position: relative; }
    .name_data label { }
    .name_data img { width: 65px; margin-left: 10px; display: inline-block; border: 2px solid #eee; }
    .name_data:hover img { border: 2px solid #444; }
    .hard_type { position: absolute; font-size: 12px; color: #aaa; letter-spacing: 0.08em; text-align: left; }
    .name_data:hover .hard_type { color: #333; }

  </style>
  <div class="main_wrap main_wrap-[!layout_style!]">


      <style>

      .difficulty_level_filter_bottom { text-align: center; width: 450px; margin: 0 auto; font-size: 12px; }
      .difficulty_level_filter_bottom .option { border: 1px solid #aaa; padding: 5px; letter-spacing: 0.2em; display: inline-block; margin: 5px; width: 115px; padding-top: 15px; }

      .difficulty_level_filter_bottom .o { letter-spacing: .3em; }

      </style>

      <div class="difficulty_level_filter_bottom"> 

        <div class="option" ng-repeat="level in difficulty_levels">
          <input type="checkbox" value="[!level.name!]" ng-model="level.selected" ng-click="toggle_level_selection(level.name)">
          &nbsp;[!level.label!]</p>
        </div><!-- . option - -->

        <p class="o">Difficulty Level</p>

      </div>  <!-- . difficulty_level_filter_bottom -->

      <hr />

      <div class="select_category_wrap filters-[!show_filters!]">
      <span class="hide_filters" ng-click="show_filters = 'no'"><i class="fa fa-close" aria-hidden="true"></i> Hide</span> 
        <div class="muscle_targeted_filter">
          <p class="side_title"><b>Muscle Targeted</b></p>
          <label class="side_list_item" ng-repeat="muscle in muscles">
          [!muscle.name!] &nbsp; 
            <input type="checkbox" value="[!muscle.name!]" ng-model="muscle.selected" ng-click="toggle_muscle_selection(muscle.name)"></label>
        </div><!-- . muscle_targeted_filter -->
        <hr />
        <div class="equipment_type_filter">
          <p class="side_title"><b>Equipment Type</b></p>
          <label class="side_list_item" ng-repeat="equipment in equipments">
          [!equipment.name!] &nbsp;
            <input type="checkbox" value="[!equipment.name!]" ng-model="equipment.selected" ng-click="toggle_equipment_selection(equipment.name)"><br>   
          </label>
        </div><!-- . equipment_type_filter --> 
        
      </div><!-- . select_category_wrap -->

  <div class="item_name_list">
    <div class="name_wrap" ng-repeat="item in display_data">
      <a ng-href="/exercise_detail/?data_id=[!item.data_id!]">
        <div class="name_data">
        <div class="hard_type">[!item.difficulty_level!]
        <p>[!item.muscle_targeted!]</p></div>
        <label>[! item.exercise_name !]</label>
        <img ng-src="/render_img?exercise?thumb?[!item.data_id!]">
        </div><!-- . name_data -->
       </a>
      </div><!-- . name_wrap - -->
  </div><!-- . item_name_list - -->

  <div class="exercise_list_wrap">
  <div class="exercise_list_data_top">

  <div class="filter_button_wrap">
    <button ng-click="show_filters = 'yes'" ng-hide="show_filters=='yes'">Filters</button>
  </div><!-- . filter_button_wrap - -->

  <style>
    .item_wrap { min-width: 380px; max-width: 450px; margin: 0 auto; }
    .exercise_data { position: relative; background-color: #fff; border-left: 1px solid red; margin-bottom: 2px; }
    .img_wrap { width: 25%; margin-left: 10px; margin-right: 10px; margin-bottom: 15px; text-align: right; }
    .img_wrap img { max-width: 100px; vertical-align: middle; }
    .text_wrap { text-align: left; min-width: 150px; }
    .text_wrap p { font-size: 12px; margin: 5px auto; }
    .img_wrap, .text_wrap { display: inline-block; vertical-align: top; }
    .item_name { font-size: 16px; color: black; text-align: left; margin-left: 15px; padding-top: 10px; padding-bottom: 10px; }

    .show_button { cursor: pointer; border: 1px solid #ccc; border-radius: 3px; width: 100px; text-align: center; padding: 15px; font-size: 14px; color: white; margin: 0 auto; }
    .show_button:hover { color: #bbb; border: 1px solid #aaa; }


      </style>
      <div class="show_button" ng-click="select_all_muscles()" ng-show="display_data==false">Show Exercises</div>
      <div class="item_wrap" ng-repeat="item in display_data2 | filter: select_name ">
        <div class="exercise_data">
          <a ng-href="/exercise_detail/?data_id=[!item.data_id!]">
            <div class="item_name">[! item.exercise_name !]</div>
          </a>
          <div class="img_wrap">
            <img ng-src="/render_img?exercise?thumb?[!item.data_id!]">
          </div><!-- . img_wrap-->

          <div class="text_wrap">
            <p>[! item.muscle_targeted !]&nbsp; - &nbsp;  Muscle Targeted</p>
            <p>[! item.equipment_type !] &nbsp; - &nbsp; Equipment Type</p> 
            <p>[! item.difficulty_level !] &nbsp; - &nbsp; Level</p>
            <p class="open_button"><a ng-href="/exercise_detail/?data_id=[!item.data_id!]"><button>Open</button></a></p>
          </div><!-- . text_wrap -->

        </div><!-- . exercise_data -->
      </div><!-- . item_wrap - -->

      </div><!-- . select_data_wrap -->

      </div><!-- . exercise_list_data_top - -->
      </div><!-- . exercise_list_wrap - -->
  </div><!-- . main_wrap -->
<style>
.find_amount {  }
.control_bar_bottom { background-color: #fff; position: fixed; left: 0; right: 0; bottom: 50px; height: 75px; border-top: 1px solid #999; }

.select_all_wrap_bottom { text-align: center; width: 225px; margin: 0 auto; font-size: 12px; position: fixed; right: 0; bottom: 55px;  }
.select_all_wrap_bottom .option { letter-spacing: 0.2em; display: inline-block; width: 100px; }

.select_all_wrap_bottom .o { letter-spacing: .07em; }

.bottom_top { border-bottom: 1px solid red; height: 35px; background-color: #444; width: 100%; }

.search_wrap { display: inline-block; font-size: 12px; padding: 5px; margin-left: 15px; }
.search_wrap input { height: 16px; padding-left: 10px; width: 175px; }

.control-desktop { left: 175px; bottom: 0; }
.control-desktop .select_all_wrap_bottom { bottom: 0; }


</style>
  <div class="control_bar_bottom control-[!layout_style!]">
  <div class="bottom_top">
    <div class="search_wrap">
    <form ng-submit='sel_by_name()'>
      <label>Seach by Name:</label> &nbsp;
      <input type="text" placeholder="e.g. Push Ups" ng-model='select_name' ng-change='sel_by_name()'>
    </form>
  </div><!-- . search_wrap - -->
  </div><!-- . bottom_top - -->
  <div class="find_amount">Showing [! (display_data| filter: select_name).length !] exercise/s</div>
    <div class="select_all_wrap_bottom">
        <div class="option">
          <p>None &nbsp; <input type="radio" name="select_all" value="deselect_all" ng-click="deselect_all_muscles()"></p>
        </div><!-- . option - -->
        <div class="option">
          <p>All &nbsp; <input type="radio" name="select_all" value="all" ng-click="select_all_muscles()"></p>
        </div><!-- . option - -->
      </div><!-- . select_all_wrap_bottom - -->
  </div><!-- . control_bar_bottom - -->
'''













sport_specific_page_code = '''
<style>
.page_ { width: 450px; margin: 0 auto; margin-top: 75px; }

.page_ img { max-width: 100%; }

</style>
<div class="page_">
<p>Sport Specific Training</p>

<img src="../../pics/home_promo_slide_moto_a.jpg" />


   <div><ul>
    <li><a href="../../sport_specific/motocross">Motocross</a></li>
    <li><a href="../../sport_specific/skiing">Skiing</a></li>
    <li><a href="../../sport_specific/snowboarding">Snowboarding</a></li>
    <li><a href="../../sport_specific/soccer">Soccer</a></li>
    <li><a href="../../sport_specific/surfing">Surfing</a></li>
    <li><a href="../../sport_specific/more"> . . & more</a></li>
  </ul></div>


</div><!-- . page_ - -->

'''



