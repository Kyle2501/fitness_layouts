# -*- coding: latin-1 -*-
# - HTML Page Code




public_nav_html = '''
  <nav class="main_nav">
    <ul>
      <a href="../../programs"><li id="programsNav">Programs</li></a>
      <a href="../../sport_specific"><li id="sport_specificNav">Sport Specific</li></a>
      <a href="../../exercises"><li id="exercisesNav">Exercise Library</li></a>
      <a href="../../free_weekly"><li id="free_weeklyNav">Free Weekly</li></a>
      <a href="../../results"><li id="resultsNav">Results</li></a>
      <a href="../../about"><li id="aboutNav">About</li></a>
      <a href="/contact"><li id="contactNav">Contact</li></a>
    </ul>
    <div class="social_wrap">
      <a href="https://www.instagram.com/shannycohen_fitness/" target="_blank"><i class="fa fa-instagram"></i></a>
      <a href="https://twitter.com/shannycohen_fit" target="_blank"><i class="fa fa-twitter-square"></i></a>
      <a href="https://www.facebook.com/ShannyCohenFitness" target="_blank"><i class="fa fa-facebook-official"></i></a>
    </div><!-- . social_wrap - -->
  </nav><!-- - /main_nav - -->
'''





main_page_html = '''
<style>
body { background: url("pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }
.page_data-desktop {  margin: 0 auto; margin-left: 200px; margin-top: 5px; margin-bottom: 175px; }
.page_data-mobile { width: 99%; margin-left: 0; margin: 0 auto; margin-top: 75px; margin-bottom: 175px; }

header.hi img { width: 75px; }
header.hi img.banner { width: 100%; }

.slides img { width: 100%; }

.slide_wrap a { color: #eee; }
.slide_text a { text-decoration: underline; }
ul.slides { padding: 0; }

ul.slides li { position: relative; list-style: none; }
.slide_text { color: #fff; font-size: 16px; padding: 10px; }

.slide_wrap { min-height: 225px;  margin-bottom: 25px; background-color: rgba(0,0,0,0.7); }
.slide_data { position: relative; min-height: 225px; }
.slide_data .slide_text { color: #fff; }
.slide_data .slide_text ul { margin-top: 15px; margin-left: 10px; }
.slide_data .slide_text ul li { font-size: 14px; list-style: disc; margin-bottom: 5px; }
.slide_button { position: absolute; bottom: 25px; right: 25px; }


.area_title { font-weight: bold; color: black; background-image: linear-gradient(to right, #444, #fff, #eee); font-size: 18px; padding: 10px; width: 205px; }

.sport_photos img { width: 150px; margin-right: 10px; }


.slide_video_data { width: 200px;  }

.video_data { width: 350px; }

.about_slide img { width: 250px; }

.library_items { width: 300px; margin: 0 auto; padding-bottom: 50px; }
.library_items img { width: 125px; margin: 10px; }

@media screen and (min-width: 550px) {
.list_wrap { margin: 0 auto; width: 450px; }
}

@media screen and (min-width: 700px) {
header.hi img { width: 100px; }
.slide_video_wrap { right: 125px; }
.slide_text { position: absolute; top: 15px; left: 15px; font-size: 24px;  }
.list_wrap { width: 750px; }
.library_items { width: 450px; position: absolute; right: 100px; bottom: 20px; }
.slide_video_wrap { position: absolute; right: 150px; bottom: 10px; }

.sport_photos { position: absolute; bottom: 25px; right: 90px; }
img.about_slide { width: 350px; }
.library_items img { width: 75px; margin: 5px; }


}


@media screen and (min-width: 750px) {



.area_title { font-size: 16px; padding: 5px; padding-left: 15px; width: 175px; }
.list_wrap { width: 700px; }
.library_items { right: 50px; width: 400px; padding-bottom: 0; }
.library_items img { width: 55px; margin: 5px; }

.sport_photos img { width: 125px; margin-right: 10px; }

.about_slide { right: 100px; bottom: 50px; }
.about_slide img { width: 225px; }

}

@media screen and (min-width: 900px) {
.list_wrap { width: 850px; }

header.hi img.banner { width: 500px; }

.library_items { width: 450px; right: 95px; }
.library_items img { width: 75px; margin: 5px; }


}

header.hi img.mark { margin-bottom: 15px; margin-right: 35px; }

.library_items img:hover { outline: 1px solid #777; }


.join_wrap { margin: 0 auto; width: 350px; }
.join_wrap div { border: 1px solid #777; text-align: center; width: 150px; border-radius: 4px; padding: 10px; }
.sign_up_button { margin-bottom: 25px; }
.apply_button {  }
.apply_button span { font-size: 14px; }

.control_buttons { position: absolute; right: 500px; bottom: 50px; text-align: right; }
.control_buttons button { }

.programs_title { color: #000; text-align: center; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), white, rgba(0, 0, 0, 0)); letter-spacing: 5px; line-height: 50px; }

</style>
  <div class="page_data-[!layout_style!]">
<!--   <header class="hi">
     <img class="mark" src="../../pics/main_logo.png" />
     <img class="banner" src="../../pics/shanny_home_banner.png" />
   </header>
-->

  <h2 class="programs_title">Shanny Cohen Fitness</h2>


  <div id="main" role="main">
      <section class="slider">
        <div class="flexslider list_wrap">
          <ul class="slides">
          
          <li class="slide_wrap">
              <div class="slide_data">
                <div class="slide_text">
                  <div class="area_title">Exercise Library</div><ul>
                    <li>Muscle Groups</li>
                    <li>Difficulty Levels</li>
                    <li>Equiptment Type</li>
                    <li>Instructional Videos</li>
                    <li>Custom Programs</li>
                </ul>
                </div><!-- . slide_text - -->
                  <div class="library_items">
                    <a href="../../exercise_detail/?data_id=20160514180309"><img src="../../pics/home_library_1.jpeg" /></a>
                    <a href="../../exercise_detail/?data_id=20161218143034"><img src="../../pics/home_library_2.jpeg" /></a>
                    <a href="../../exercise_detail/?data_id=20160420160141"><img src="../../pics/home_library_3.jpeg" /></a>
                    <a href="../../exercise_detail/?data_id=20161216143334"><img src="../../pics/home_library_4.jpeg" /></a>
                    <a href="../../exercise_detail/?data_id=20160522224613"><img src="../../pics/home_library_5.jpeg" /></a>
                    <a href="../../exercise_detail/?data_id=20161218120311"><img src="../../pics/home_library_6.jpeg" /></a>
                    <a href="../../exercise_detail/?data_id=20160515220309"><img src="../../pics/home_library_7.jpeg" /></a>
                    <a href="../../exercise_detail/?data_id=20161128200430"><img src="../../pics/home_library_8.jpeg" /></a>
                    <a href="../../exercise_detail/?data_id=20160519222305"><img src="../../pics/home_library_9.jpeg" /></a>
                    <a href="../../exercise_detail/?data_id=20161202000706"><img src="../../pics/home_library_0.jpeg" /></a>
                  </div><!-- . library_items - -->
                <a href="../../exercises"><div class="slide_button">Open</div></a>
              </div><!-- . slide_data - -->
            </li>
          
            <li class="slide_wrap" data-thumb="../../pics/exercise_thumb.jpg">
              <div class="slide_data">
                <div class="slide_text">
                <div class="area_title">Free Weekly Workout</div></div>
                <div class="control_buttons">
                    <button type="button" id="play-pause">Play<i class="fa fa-play"></i></button>
                    <br /><button type="button" id="mute">Mute<i class='fa fa-volume-off'></i></button>
                    <br /><button type="button" id="full-screen">Full Screen<i class="fa fa-expand"></i></button>
                  </div><!-- . control_buttons - -->
                <div class="slide_video_wrap">
                  <div class="video_data" ng-show='item_focus.video_key'>
                    <video id="video" width="100%" height="175" ng-src="[!video_url!]">
                    </video><div class="progress_bar"><input type="range" id="seek-bar" value="0"></div>
                  </div><!-- . slide_video_data - -->
                  
        

            <div class="volume_controls">
            <!--
            <input type="range" id="volume-bar" min="0" max="1" step="0.1" value="1"> -->
            </div>
                  
                </div><!-- . slide_video_wrap - -->

                <a href="../../free_weekly"><div class="slide_button">Open</div></a>
              </div><!-- . slide_data - -->
            </li>



            <li class="slide_wrap" data-thumb="../../pics/home_promo_slide_moto_a.jpg">
              <div class="slide_data">
              <div class="slide_text">
                <div class="area_title">Sport Specific Training</div><ul>
                <li>Motocross</li>
                <li>Skiing</li>
                <li>Snowboarding</li>
                <li>Soccer</li>
                <li>Surfing</li>
              </ul></div>
              <div class="sport_photos">
                <img src="../../pics/sport_photo_d.jpeg" />
                <img src="../../pics/sport_photo_e.jpeg" />
                <img src="../../pics/sport_photo_b.jpeg" />
              </div>
              <a href="../../sport_specific"><div class="slide_button">Open</div></a>
              </div><!-- . slide_data - -->
            </li>
            

            <li class="slide_wrap" data-thumb="../../pics/results_thumb.jpg">
              <div class="slide_data">
              <div class="slide_text">
                <div class="area_title">About Shanny</div><ul>
                <li>ACE Certified Personal Trainer</li>
                <li><a href="https://shannycohen.com/sponsors/" target="_blank">Sponsored</a> &amp; <a href="https://shannycohen.com/exposure/" target="_blank">Published</a> Athelete</li>
                <li>Competitively Ranked Ski <a href="https://shannycohen.com/accomplishments/" target="_blank">Champion</a></li>
              </ul></div>
              <div class="slide_video_wrap about_slide">
                <img src="../../pics/about.jpg" />
                  <div class="slide_video_data"></div>
                </div><!-- . slide_video_wrap - -->

              <a href="../../about"><div class="slide_button">Open</div></a>
              </div><!-- . slide_data - -->
            </li>

          </ul>
        </div>
      </section>
      <div class="join_wrap">
        <a href="../../programs"><div class="sign_up_button">Sign Up Now</div></a>
        <div class="apply_button">Apply <span>for the</span> Waitlist</div>
      </div><!-- . join_wrap - -->
    </div><!-- . main - -->


  </div><!-- - /page_html - -->
'''




bikini_bootcamp_page_html = '''<style>
.page_data-desktop { width: 800px; margin: 0 auto; margin-left: 200px; margin-top: 5px; margin-bottom: 175px; }
.page_data-mobile { width: 99%; margin-left: 0; margin: 0 auto; margin-top: 75px; margin-bottom: 175px; }
</style>
<div class="page_data-[!layout_style!]">


<div>Bikini Bootcamp</div>



</div><!-- . page_data - -->
'''




free_weekly_page_html = '''<style>
body { background: url("pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }

.page_data-desktop { width: 800px; margin: 0 auto; margin-left: 200px; margin-top: 5px; margin-bottom: 175px; }
.page_data-mobile { width: 99%; margin-left: 0; margin: 0 auto; margin-top: 75px; margin-bottom: 175px; }

.video_main { margin-top: 25px; color: #fff; }
.focus_item { margin-top: 5px; }
.focus_data { border: 1px solid #eee; padding: 10px; line-height: 12px; margin: 5px; display: inline-block; }
.video_data { display: inline-block; vertical-align: top; width: 400px; margin-top: 25px; }

.video_error { width: 275px; display: inline-block; }
.player_wrap { background-color: rgba(0,0,0,0.7); outline: 1px solid #eee; padding: 10px; margin-top: 15px; }

.video_list { margin-top: 75px; }

.area_title { font-weight: bold; color: black; background-image: linear-gradient(to right, #444, #fff, #aaa); font-size: 18px; padding: 10px; width: 205px; }
.area_title span { font-size: 16px; margin-left: 5px; color: #999; }


.list_item { display: inline-block; width: 50%; vertical-align: top; }
.item_data { padding: 10px; line-height: 12px; background-color: rgba(0,0,0,0.7); outline: 1px solid #eee; margin: 5px; position: relative; color: #fff; }
.item_name {  }
.item_week { font-size: 14px; }
.item_date { font-size: 14px; }
</style>
<div class="page_data-[!layout_style!]">



<div class="video_main">


<div class="area_title">Free Weekly Workout</div>

<div class="player_wrap">
<div class="focus_item">
  
   <div class="video_error" ng-show='!item_focus.video_key'>No Video</div>
      <div class="video_data" ng-show='item_focus.video_key'>
        <video id="video" width="100%" height="200" ng-src="[!video_url!]"></video>
      </div><!-- . video_data -->
      

  
  <div class="focus_data">
    <p class="item_name">[!item_focus.video_name!]</p>
    <p class="item_week">Week # [!item_focus.video_week!]</p>
    <p class="item_date">Published on [!item_focus.video_date!]</p>
  </div><!-- . focus_data - -->
  
  <div class="control_buttons" ng-show='item_focus.video_key'>
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
  

</div><!-- . focus_item - -->
</div><!-- . player_wrap - -->

</div><!-- . video_main - -->

<div class="video_list">
<p class="area_title">Video List,<span> past weeks</span></p>
<div class="list_item" ng-repeat="item in item_list">
  <div class="item_data">
    <div class="item_photo"><img ng-src="/render_img?weekly_video?thumb?[!item.data_id!]"></div>
    <p class="item_name">[!item.video_name!]</p>
    <p class="item_week">Week # [!item.video_week!]</p>
    <p class="item_date">Published on [!item.video_date!]</p>
  </div><!-- . item_data - --></div><!-- . list_item - -->
</div><!-- . video_list - -->


</div><!-- . page_data - -->
'''









main_page_html_old = '''
<link rel="stylesheet" href="../files/flexslider.css" type="text/css" media="screen" />
<style>

.page_data-desktop { width: 800px; margin: 0 auto; margin-left: 200px; margin-top: 5px; margin-bottom: 175px;  }
.page_data-mobile { width: 99%; margin-left: 0; margin: 0 auto; margin-top: 75px; margin-bottom: 175px;  }

header.hi img { width: 75px; }

ul.slides li { position: relative; }
.slide_text { position: absolute; top: 35px; left: 15px; color: #fff; font-size: 12px; }
@media screen and (min-width: 600px){
  header.hi img { width: 145px; }
  .slide_text { font-size: 24px; }
}
</style>
  <div class="page_data-[!layout_style!]">
   <header class="hi"><span class="color_b"><img src="../../pics/main_logo.png" /></span></header>

  <div id="main" role="main">
      <section class="slider">
        <div class="flexslider">
          <ul class="slides">
            <li data-thumb="../../pics/home_promo_slide_moto_a.jpg">
              <a href="../../sport_specific/snowboarding"><img src="../../pics/home_promo_slide_moto_a.jpg" /></a>
              <div class="slide_text"><b>Highlight!</b> <br />Sport Specific Training<br />SNOWBOARDING<br />Pro Athlete Danny Toumarkine</div>
            </li>
             <li data-thumb="../../pics/exercise_thumb.jpg">
              <a href="../../exercises"><img src="../../pics/exercise_thumb.jpg" /></a>
              <div class="slide_text">Free Workout</div>
            </li>
             <li data-thumb="../../pics/programs_thumb.jpg">
              <a href="../../about"><img src="../../pics/programs_thumb.jpg" /></a>
              <div class="slide_text">Work Experience</div>
            </li>
            <li data-thumb="../../pics/results_thumb.jpg">
              <a href="../../about"><img src="../../pics/results_thumb.jpg" /></a>
              <div class="slide_text">About Shanny</div>
            </li>

          </ul>
        </div>
      </section>
    </div>


  <!-- jQuery -->
  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>


  <!-- FlexSlider -->
  <script defer src="../../files/jquery.flexslider-min.js"></script>

  <script type="text/javascript">
    $(window).load(function(){
      $('.flexslider').flexslider({
        animation: "slide",
        controlNav: "thumbnails",
        start: function(slider){
          $('body').removeClass('loading');
        }
      });
    });
  </script>


  </div><!-- - /page_html - -->
'''








programs_page_html = '''
  <style>
  body { background: url("pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }
  .programs_title { color: #000; text-align: center; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), white, rgba(0, 0, 0, 0)); letter-spacing: 5px; line-height: 50px; }
  .package_list { width:90%; text-align: center; margin: 10px; }
  .package_wrap { background: rgba(0, 0, 0, 0.8); display: inline-block; text-align: center; width: 40%; max-width: 400px; margin: 20px auto; vertical-align: top; padding: 20px; color: #bbb; }
  .package_wrap ul { padding-left: 20px;}
  .package_wrap li { text-align: left; font-size: 14px; margin-bottom: 5px; padding: 5px; }
  .package_title { color: black; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), white, rgba(0, 0, 0, 0)); }
  .package_info { background: rgba(255, 255, 255, 0.1); padding: 10px; }
  .sign_up_text { color: red; font-size:16px; }
  .sign_up_btn { border:none; border-radius: 0; padding: 5px; font-size: 14px; margin: 0 5px; }
  .sign_up_btn:hover{background:#ccc;}
  .white { color: #fff; }
  @media screen and (max-width: 1000px){
    body { background: linear-gradient(90deg, #555, #333); }
    .package_wrap {width:90%; margin: auto; };
  }
  </style>
  
  <div class="main_wrap-[!layout_style!]">
    <div class="package_list">
    
    <h2 class="programs_title">Memberships</h2>
    
    <div class="package_wrap">
        <div class="package_data">
          <h2 class="package_title"><b>Bronze</b></h2>
          <p class="package_price">$55/month
          <br />$13.75/week
          <br />$4.58/workout
          </p>
          <p class="package_info">3x a week Total Body Training
          <br />Customized to your fitness level
          <br />Full access to the Exercise Library
         </p>
          <ul class="package_bullet">
            <li><span class="white">Focus on muscle definition, strength, endurance, weight loss, flexibility and balance</span></li>
                      </ul>
        </div><!-- . package_data - -->
        <button class="sign_up_btn" ng-click=" confirm_signup('Bronze'); ">Sign Up</button>
      </div><!-- . package_wrap - -->
    
    
      <div class="package_wrap">
        <div class="package_data">
          <h2 class="package_title"><b>Silver</b></h2>
          <p class="package_price">$80/Month</p>
          <p class="package_info">5 workouts a week emailed directly to you.</p>
          <ul class="package_bullet">
            <li><span class="white">3 workout lifting videos</span></li>
            <li>1 HIIT(High Intensity Interval Training) / class / abs</li>
            <li>Recovery, myofacial release, flexibility and balance work</li>
            <li>Focus on muscle definition, strength, endurance, weight loss, flexibility and balance</li>
          </ul>
        </div><!-- . package_data - -->
        <button class="sign_up_btn" ng-click="confirm_signup('Silver'); ">Sign Up</button>
      </div><!-- . package_wrap - -->

      
      
      <h2 class="programs_title">Personalized Packages</h2>
      <div class="package_wrap">
        <div class="package_data">
          <h2 class="package_title"><b>Platinum</b></h2>
          <p class="package_price">$200/Month</p>
          <p class="package_info"> 7 day a week program that is fully customized to each clients goals, fitness level, physical injuries and health conditions.</p>
          <ul class="package_bullet">
            <li>Written workout available online or <span class="white">printable daily</span>. Weekly workouts posted or emailed Sunday nights.</li>
            <li>Personalized daily video of the focus for each exercise</li>
            <li>Start and end point photos of each written exercise</li>
            <li>Check in and feedback reports with Shanny throughout the week</li>
            <li>Customized to your fitness goals</li>
          </ul><!-- . package_list - -->
        </div><!-- . package_data - -->
        <div>
          <p class="sign_up_text">* Limited Spots Available</p>
          <button class="sign_up_btn" ng-disabled='platinum_avail' ng-click=" confirm_signup('Platinum') ">Sign Up</button>
          <button class="sign_up_btn" ng-disabled='!platinum_avail' ng-click=" add2waitlist('Platinum') ">Add to Waitlist</button>
        </div>
      </div><!-- . package_wrap - -->

      <div class="package_wrap">
        <div class="package_data">
          <h2 class="package_title"><b>Gold</b></h2>
          <p class="package_price">$100/Month</p>
          <p class="package_info"> 3 day a week program that is fully customized to each clients goals, fitness level, physical injuries and health conditions.</p>
          <ul class="package_bullet">
            <li>Written workout available online or <span class="white">printable three times a week</span>. Weekly workouts posted or emailed Sunday nights.</li>
            <li>Personalized daily video of the focus for each exercise</li>
            <li>Start and end point photos of each written exercise</li>
            <li>Check in and feedback reports with Shanny throughout the week</li>
            <li>Customized to your fitness goals </li>
          </ul>
        </div><!-- . package_data - -->
        <div>
          <p class="sign_up_text">* Limited Spots Available</p>
          <button class="sign_up_btn" ng-disabled='gold_avail' ng-click=" confirm_signup('Gold') ">Sign Up</button>
          <button class="sign_up_btn" ng-disabled='!gold_avail' ng-click=" add2waitlist('Gold') ">Add to Waitlist</button>
        </div>
      </div><!-- . package_wrap - -->


    </div><!-- . package_list -—>

  </div><!-- . main_wrap -->
'''


about_page_html = '''<style>
  body { background: url("pics/bg_p_01.jpg") no-repeat center center fixed; background-size: cover; }
  .page_title { color: #000; text-align: center; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), white, rgba(0, 0, 0, 0)); letter-spacing: 5px; height: 40px; padding-top: 5px; }
    .package_list { text-align: center; padding-top: 30px; }
  .about_blurb { background: rgba(0, 0, 0, 0.8); display: inline-block; text-align: justify; margin: 20px; vertical-align: top; padding: 30px; width: 350px; }
  .blurb_header1 { background: url("pics/about_section.png"); padding: 50px; no-repeat center center; background-size: cover; }
  .blurb_header2 { background: url("pics/about_section2.png"); padding: 50px; no-repeat center center; background-size: cover; }
  .blurb_heading { text-shadow: 2px 2px #000; }
  p { line-height: 20px; padding-top: 10px; }
  @media screen and (max-width: 800px){
    body { background: linear-gradient(90deg, #555, #333);}
  }
  </style>

  <div class="main_wrap-[!layout_style!]">
    <h2 class="page_title">About Me</h2>
    <div class="about_blurb">
    <div class="blurb_header1"><h2 class="blurb_heading">Personal</h2></div>
    <p>Shanny at 26 years old has 6 years of experience as an ACE Certified Personal Trainer and Orthopedic Exercise Specialist. She was raised in Sun Valley, ID as a competitive alpine ski racer amongst other sports such as soccer, tennis, dirtbike riding and wakesurfing. Skiing as a top level competitor she was in the gym 5 days a week to maintain top physical condition for her ski career. After making the US Alpine Development System, she soon after retired and moved on to compete as a professional freeskier for the following 6 years. At the end of her career in 2010 she was ranked 9th in the world for female slopestyle skiing. </p>
    <p>As her career ended, she was inspired to help the younger athletes achieve their best physical fitness level in order to meet the demands of professional competition. She received her certification as a personal trainer and orthopedic exercise specialist through ACE (American Council on Exercise) and moved back to Ketchum, ID to begin her training. </p>
    </div>

    <div class="about_blurb">
    <div class="blurb_header2"><h2 class="blurb_heading">Work Experience</h2></div>
    <p>Shanny works with clients ranging from professional athletes to men and women who have never stepped foot in a gym before. She specializes with athletic performance training, strength and conditioning, exercise rehab, injury prevention and weight loss. Through her Orthopedic Exercise Specialty Certification she is qualified for exercise rehab specializing with the low back, the knee and shoulder. Whether its joint replacement, post surgery exercise rehabilitation, or injury prevention, she has done it all. Weight loss training and becoming leaner to show better muscle definition is a highlight of many of the programs she builds. Strength and Conditioning programs help not only with physical conditioning, but the focus on applying movements into every day life activities. Seeing the changes in your body composition and muscle tone with this program has been proven to be extremely successful.</p>
    <p>Shanny is a trainer who is very adamant about proper form in each exercise and progression in a safe and effective manner. Platinum and Gold programs take the physical condition, physical training experience and personalized goals into account when building the program. Any health aliments and/or limitations are addressed. </p>
    <p>If you’ve been lacking motivation, not seeing the results you want, and wanting to be at the top of your game, Shanny will make that possible. With your commitment of hard work, and her program designs, she promises you will see the results you thought were unattainable. We look forward to helping you reach and exceed your goals here at Shanny Cohen Fitness.  </p>
    </div>
  </div><!-- . main_wrap - -->
'''



#----------------------------------------------#
#        Results and Testimonials              #
#----------------------------------------------#
results_page_html = '''


  <style type="text/css">
  body { background: url("pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }
    pre { white-space: pre-wrap; white-space: -moz-pre-wrap; white-space: -pre-wrap;  white-space: -o-pre-wrap; word-wrap: break-word; }
    .testimonial_wrap{ border: 1px solid grey; border-radius: 3px; text-align: left; padding: 20px; margin: 0 auto; margin-bottom: 25px; width: 325px; display: block; background: rgba(0, 0, 0, 0.8); vertical-align: top; color: #fff; min-height: 175px; }
    .show_btn { color: steelblue;  }
    .testimonial_thumb { max-width: 100px; }
    .modal-backdrop { position: fixed; top: 0; left: 0; bottom: 0; right: 0;  z-index: 150;  background:rgba(0,0,0, 0.6); }
    .modal{ position: absolute; top: 25px; z-index: 200; text-align: center; margin: auto auto; max-height:90%; max-width: 90%; }
    #lg_img { max-height: 90%; max-width: 90%; margin: auto auto; }
    header.hi { color: #000; text-align: center; }

    .list_wrap { max-width: 800px; margin: 0 auto; }

    .top_text { color: #777; }

    .main_wrap-mobile li {  }

    @media (min-width: 850px) {
      .testimonial_wrap { margin: 15px; display: inline-block;  }

    }


    </style>
  <div class="main_wrap-[!layout_style!]">
    <header class="hi">Results and Testimonials</header>

    <div class="modal-backdrop" ng-show="modal_show"></div>
    <div class="modal" ng-show="modal_show">
      <img id="lg_img" ng-src='[!lg_img_url!]'>
      <button ng-click="hide_lg_img()">Close</button>
    </div>

    <div class="list_wrap">

    <div class="testimonial_wrap" ng-repeat="item in testimonial_data | orderBy: '-add_time'">
      <testimonial-view data="item"></testimonial-view>
    </div><!-- . testimonial_wrap -->

  </div><!-- . list_wrap - -->
  </div><!-- . main_wrap - -->
'''



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

    .button_wrap { display: inline-block; margin: 10px; border: 1px solid #aaa; border-radius: 3px; padding: 5px; width: 85px; text-align: center; cursor: pointer; font-size: 12px; font-family: 'Lato', sans-serif; background-color: white; }
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


     <div class="button_wrap"><label>
      <input type="checkbox" name="deselect_all" value="deselect_all" ng-click="deselect_all_muscles()" class="hide"> Deselect<br>        
     </label></div>


     <div class="button_wrap"><label>
        <input type="checkbox" name="select_all" value="all" ng-click="select_all_muscles()" class="hide"> Select All<br>
      </label></div>

    
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





sport_specific_page_code = '''
<style>
body { background: url("pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }
.page_ { max-width: 800px; margin: 0 auto; margin-top: 75px; }

.page_ img { max-width: 100%; }

.sub_nav_wrap1 { margin-left: 35px; display: inline-block; vertical-align: top; margin-top: 0; }
.sub_nav_wrap1 li { margin-bottom: 5px; list-style: none; }
.sub_nav_wrap1 ul li a { color: #fff; }
.sub_nav_wrap1 ul li a:hover { color: #bbb; }
.sub_nav_wrap1 ul { padding: 0; margin: 0; }
.sign_up_button { display: inline-block; padding-top: 65px; margin-right: 75px; vertical-align: top; margin-left: 50px; }
.sub_nav_wrap1 ul li:hover { list-style: disc; color: red; }

.package_list_wrap {  }

header.hi { text-align: center; color: #000; }

.mid_section { max-width: 485px; margin: 0 auto; background-color: rgba(0,0,0,0.5); color: #aaa; padding: 15px; border: 1px solid white; }

@media screen and (max-width: 800px){
  .sub_nav_wrap1 { margin-left: 0; }
  .sign_up_button { margin-left: 20px; }
}

</style>
<div class="page_">

  

<header class="hi"><span class="color_b">Sport Specific Training</span></header>
<p style="text-align:center;"><img src="../../pics/home_promo_slide_moto_a.jpg" /></p>
<p>Pro Athlete &nbsp; <b>Danny Toumarkine</b></p>



<div class="package_list_wrap">
<div class="package_bullet"><ul>
    <li>Written workout available online or printable daily. Weekly workouts posted or emailed Sunday nights.</li>
    <li>Personalized daily video of the focus for each exercise</li>
    <li>Start and end point photos of each written exercise</li>
    <li>Check in and feedback reports with Shanny throughout the week</li>
    <li>Customized to your fitness goals</li>
  </ul><!-- . package_list - --></div>
</div>



</div><!-- . page_ - -->

'''



sport_specific_motocross_page_code = '''
<style>
body { background: url("../../pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }


</style>

<div class="sub_nav_wrap" ng-if="layout_style=='desktop'"><ul>
    <li class="motocrossSubNav"><a href="../../sport_specific/motocross">Motocross</a></li>
    <li class="skiingSubNav"><a href="../../sport_specific/skiing">Skiing</a></li>
    <li class="snowboardingSubNav"><a href="../../sport_specific/snowboarding">Snowboarding</a></li>
    <li class="soccerSubNav"><a href="../../sport_specific/soccer">Soccer</a></li>
    <li class="surfingSubNav"><a href="../../sport_specific/surfing">Surfing</a></li>
  </ul></div>

<div class="page_wrap-[!layout_style!]">
<header class="hi"><span class="color_b">Sport Specific Training</span></header>

<p class="ss_page_name">Motocross</p>

<div class="ss_top_wrap">

<div class="ss_photo">
  <p><img src="../../pics/sport_moto_photo_a.jpg" /></p>
  <p>Pro Athlete &nbsp; <b></b></p>
</div><!-- . ss_photo - -->

<div class="package_list_wrap">
  <ul class="package_bullet">
    <li>Written workout available online or printable daily. Weekly workouts posted or emailed Sunday nights.</li>
    <li>Personalized daily video of the focus for each exercise</li>
    <li>Start and end point photos of each written exercise</li>
    <li>Check in and feedback reports with Shanny throughout the week</li>
    <li>Customized to your fitness goals</li>
  </ul><!-- . package_list - -->

  <div class="sign_up_button">
    <a href="../../contact"><button>Sign Up Now</button></a>
  </div>
</div>

</div><!-- . top_wrap - -->

</div><!-- . page_ - -->

'''



sport_specific_skiing_page_code = '''
<style>
body { background: url("../../pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }

</style>

<div class="sub_nav_wrap" ng-if="layout_style=='desktop'"><ul>
    <li class="motocrossSubNav"><a href="../../sport_specific/motocross">Motocross</a></li>
    <li class="skiingSubNav"><a href="../../sport_specific/skiing">Skiing</a></li>
    <li class="snowboardingSubNav"><a href="../../sport_specific/snowboarding">Snowboarding</a></li>
    <li class="soccerSubNav"><a href="../../sport_specific/soccer">Soccer</a></li>
    <li class="surfingSubNav"><a href="../../sport_specific/surfing">Surfing</a></li>
  </ul></div>

<div class="page_wrap-[!layout_style!]">

<header class="hi"><span class="color_b">Sport Specific Training</span></header>

<p class="ss_page_name">Skiing</p>

<div class="ss_top_wrap">


<div class="package_list_wrap">
  <ul class="package_bullet">
    <li>Written workout available online or printable daily. Weekly workouts posted or emailed Sunday nights.</li>
    <li>Personalized daily video of the focus for each exercise</li>
    <li>Start and end point photos of each written exercise</li>
    <li>Check in and feedback reports with Shanny throughout the week</li>
    <li>Customized to your fitness goals</li>
  </ul><!-- . package_list - -->
  <div class="sign_up_button">
    <a href="../../contact"><button>Sign Up Now</button></a>
  </div>
</div>

<div class="ss_photo">
  <p><img src="../../pics/sport_moto_photo_a.jpg" /></p>
  <p>Pro Athlete &nbsp; <b></b></p>
</div><!-- . ss_photo - -->

</div><!-- . top_wrap - -->


</div><!-- . page_ - -->

'''

sport_specific_snowboarding_page_code = '''
<style>
body { background: url("../../pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }


.title_wrap { background-color: rgba(0,0,0,0.5); padding: 15px; width: 275px; font-size: 16px; display: inline-block; padding-right: 125px; padding-left: 35px; margin-bottom: 10px; }
.ss_page_name { text-align: center; }

.discount_wrap { background-color: rgba(0,0,0,0.5); padding: 15px; width: 225px; text-align: center; font-size: 24px; display: inline-block; vertical-align: top; padding-bottom: 5px; color: white; }
.discount_wrap:hover { color: #aaa; }

.page_wrap-desktop { }

</style>

<div class="sub_nav_wrap" ng-if="layout_style=='desktop'"><ul>
    <li class="motocrossSubNav"><a href="../../sport_specific/motocross">Motocross</a></li>
    <li class="skiingSubNav"><a href="../../sport_specific/skiing">Skiing</a></li>
    <li class="snowboardingSubNav"><a href="../../sport_specific/snowboarding">Snowboarding</a></li>
    <li class="soccerSubNav"><a href="../../sport_specific/soccer">Soccer</a></li>
    <li class="surfingSubNav"><a href="../../sport_specific/surfing">Surfing</a></li>
  </ul></div>


<div class="page_wrap-[!layout_style!]">
  <header class="hi"><span class="color_b">Sport Specific Training</span></header>


  <div class="title_wrap">
    <p> <span class="ss_page_name">Snowboarding</span></p>
    <p>Pro Athlete &nbsp; <b>Danny Toumarkine</b></p>
  </div>

<a href="../../programs"><div class="discount_wrap">
  <p>20% Off Monthly Featured Program</p>
</div><!-- . discount_wrap - --></a>




  <div class="ss_top_wrap">

<div class="ss_photo">
  <p><img src="../../pics/home_promo_slide_moto_a.jpg" /></p>

</div><!-- . ss_photo - -->

<div class="package_list_wrap">
  <ul class="package_bullet">
    <li>Written workout available online or printable daily. Weekly workouts posted or emailed Sunday nights.</li>
    <li>Personalized daily video of the focus for each exercise</li>
    <li>Start and end point photos of each written exercise</li>
    <li>Check in and feedback reports with Shanny throughout the week</li>
    <li>Customized to your fitness goals</li>
  </ul><!-- . package_list - -->

  <div class="sign_up_button">
    <a href="../../contact"><button>Sign Up Now</button></a>
  </div>
</div>

</div><!-- . top_wrap - -->

</div><!-- . page_ - -->

'''


sport_specific_soccer_page_code = '''
<style>
body { background: url("../../pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }

</style>

<div class="sub_nav_wrap" ng-if="layout_style=='desktop'"><ul>
    <li class="motocrossSubNav"><a href="../../sport_specific/motocross">Motocross</a></li>
    <li class="skiingSubNav"><a href="../../sport_specific/skiing">Skiing</a></li>
    <li class="snowboardingSubNav"><a href="../../sport_specific/snowboarding">Snowboarding</a></li>
    <li class="soccerSubNav"><a href="../../sport_specific/soccer">Soccer</a></li>
    <li class="surfingSubNav"><a href="../../sport_specific/surfing">Surfing</a></li>
  </ul></div>


<div class="page_wrap-[!layout_style!]">
<header class="hi"><span class="color_b">Sport Specific Training</span></header>

<p class="ss_page_name">Soccer</p>

<div class="ss_top_wrap">

<div class="ss_photo">
  <p><img src="../../pics/sport_moto_photo_a.jpg" /></p>
  <p>Pro Athlete &nbsp; <b></b></p>
</div><!-- . ss_photo - -->

<div class="package_list_wrap">
  <ul class="package_bullet">
    <li>Written workout available online or printable daily. Weekly workouts posted or emailed Sunday nights.</li>
    <li>Personalized daily video of the focus for each exercise</li>
    <li>Start and end point photos of each written exercise</li>
    <li>Check in and feedback reports with Shanny throughout the week</li>
    <li>Customized to your fitness goals</li>
  </ul><!-- . package_list - -->

  <div class="sign_up_button">
    <a href="../../contact"><button>Sign Up Now</button></a>
  </div>
</div>

</div><!-- . top_wrap - -->

</div><!-- . page_ - -->

'''


sport_specific_surfing_page_code = '''
<style>
body { background: url("../../pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }

</style>

<div class="sub_nav_wrap" ng-if="layout_style=='desktop'"><ul>
    <li class="motocrossSubNav"><a href="../../sport_specific/motocross">Motocross</a></li>
    <li class="skiingSubNav"><a href="../../sport_specific/skiing">Skiing</a></li>
    <li class="snowboardingSubNav"><a href="../../sport_specific/snowboarding">Snowboarding</a></li>
    <li class="soccerSubNav"><a href="../../sport_specific/soccer">Soccer</a></li>
    <li class="surfingSubNav"><a href="../../sport_specific/surfing">Surfing</a></li>
  </ul></div>

<div class="page_wrap-[!layout_style!]">

<header class="hi"><span class="color_b">Sport Specific Training</span></header>

<p class="ss_page_name">Surfing</p>

<div class="ss_top_wrap">


<div class="package_list_wrap">
  <ul class="package_bullet">
    <li>Written workout available online or printable daily. Weekly workouts posted or emailed Sunday nights.</li>
    <li>Personalized daily video of the focus for each exercise</li>
    <li>Start and end point photos of each written exercise</li>
    <li>Check in and feedback reports with Shanny throughout the week</li>
    <li>Customized to your fitness goals</li>
  </ul><!-- . package_list - -->
  <div class="sign_up_button">
    <a href="../../contact"><button>Sign Up Now</button></a>
  </div>
</div>

<div class="ss_photo">
  <p><img src="../../pics/sport_moto_photo_a.jpg" /></p>
  <p>Pro Athlete &nbsp; <b></b></p>
</div><!-- . ss_photo - -->

</div><!-- . top_wrap - -->


</div><!-- . page_ - -->

'''






sport_specific_more_page_code = '''
<style>
body { background: url("../../pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }

</style>

<div class="sub_nav_wrap" ng-if="layout_style=='desktop'"><ul>
    <li class="motocrossSubNav"><a href="../../sport_specific/motocross">Motocross</a></li>
    <li class="skiingSubNav"><a href="../../sport_specific/skiing">Skiing</a></li>
    <li class="snowboardingSubNav"><a href="../../sport_specific/snowboarding">Snowboarding</a></li>
    <li class="soccerSubNav"><a href="../../sport_specific/soccer">Soccer</a></li>
    <li class="surfingSubNav"><a href="../../sport_specific/surfing">Surfing</a></li>
  </ul></div>


<header class="hi"><span class="color_b">Sport Specific Training</span></header>


<p>More</p>


<div class="sign_up_button">
    <a href="../../contact"><button>Sign Up Now</button></a>
  </div>

<div class="package_list_wrap">
  <ul class="package_bullet">
    <li>Written workout available online or printable daily. Weekly workouts posted or emailed Sunday nights.</li>
    <li>Personalized daily video of the focus for each exercise</li>
    <li>Start and end point photos of each written exercise</li>
    <li>Check in and feedback reports with Shanny throughout the week</li>
    <li>Customized to your fitness goals</li>
  </ul><!-- . package_list - -->
  <div class="sign_up_button">
    <a href="../../contact"><button>Sign Up Now</button></a>
  </div>
</div>


</div><!-- . page_ - -->

'''




contact_page_html = '''
<style>
  body { background: url("pics/e_bg_c.jpg") no-repeat center center fixed; background-size: cover; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; color: #fff; }
  input[type="text"],input[type="email"] { width: 200px; height: 16px; border-color: #777; border-style: solid; border-width: 1px; }
  textarea { width: 200px; height: 100px; }
  textarea[name="client_question"] { height: 150px; }
  .error { color: red; }
  .reCaptcha { width: 100%; }
  .form_wrap { margin: 0 auto; background: rgba(0, 0, 0, 0.3); }
  header.hi { text-align: center; color: #000; }
  .header_photo { max-width: 900px; margin: 0 auto; }
  .header_photo img { width: 100%; }

  .main_wrap-mobile .form_wrap { max-width: 400px; padding-top: 25px; padding-left: 25px; }


</style>
  <div class="main_wrap-[!layout_style!]">
    <div class="header_photo">
      <img src="../../pics/contact_page.jpg" /></div>
    <header class="hi">
      <p>Ask Shanny & Sign up for a Program</p>
    </header>
    <article class="form_wrap">
      <form ng-submit="submit_question()" method="post">
        <table>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" ng-model='item.client_name' required/></td>
          </tr>
          <tr>
            <td class="label">Email*</td>
            <td class="input"><input type="email" name="client_email" ng-model='item.client_email' required/></td>
          </tr>
          <tr>
            <td class="label">Address</td>
            <td class="input"><textarea name="client_address" ng-model='item.client_address'></textarea></td>
          </tr>
          <tr>
            <td class="label">Question*</td>
            <td class="input"><textarea name="client_question" ng-model='item.client_question' required></textarea></td>
          </tr>
        </table>
        <div class="reCaptcha">
          <div class="g-recaptcha" data-sitekey="6LcPLh4TAAAAALuK4eCSLrVwlRtxpzOy45c0fDld"></div>
        </div>
        <table>
          <tr>
            <td style="width:180px"></td>
            <td style="text-align:right"><input ng-disabled='btn_disable' type="submit" value="Submit" /></td>
          </tr>
        </table>
      </form>
      <p class="error" ng-show="if_recaptcha_error_show">Please Pass the reCaptcha Test</p>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - -->
'''

contact_success_page_html = '''
  <div class="main_wrap-[!layout_style!]">
    <h2>Your question has been submitted.</h2>
    <h2>We'll reply as soon as possible.</h2>
  </div><!-- . main_wrap -->
'''



