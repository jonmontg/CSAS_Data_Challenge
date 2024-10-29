<table border=1></th></th></th><tr ><th >column<th >description<th >data_type</tr></td></td></td><tr ><td >pitch_type<td ><div>The type of pitch derived from Statcast.
<br>
<br></div><td >Categorical(ordering='physical')</tr></td></td></td><tr ><td >game_date<td ><div>Date of the Game.
<br>
<br></div><td >Date</tr></td></td></td><tr ><td >release_speed<td ><div>Pitch velocities from 2008-16 are via Pitch F/X, and adjusted to roughly out-of-hand release point. All velocities from 2017 and beyond are Statcast, which are reported out-of-hand.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >release_pos_x<td ><div>Horizontal Release Position of the ball measured in feet from the catcher's perspective.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >release_pos_z<td ><div>Vertical Release Position of the ball measured in feet from the catcher's perspective.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >player_name<td ><div>Player's name tied to the event of the search.
<br>
<br></div><td >Categorical(ordering='physical')</tr></td></td></td><tr ><td >batter<td ><div>MLB Player Id tied to the play event.
<br>
<br></div><td >UInt32</tr></td></td></td><tr ><td >pitcher<td ><div>MLB Player Id tied to the play event.
<br>
<br></div><td >UInt32</tr></td></td></td><tr ><td >events<td ><div>Event of the resulting Plate Appearance.
<br>
<br></div><td >Categorical(ordering='physical')</tr></td></td></td><tr ><td >description<td ><div>Description of the resulting pitch.
<br>
<br></div><td >Categorical(ordering='physical')</tr></td></td></td><tr ><td >zone<td ><div>Zone location of the ball when it crosses the plate from the catcher's perspective.
<br>
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >des<td ><div>Plate appearance description from game day.
<br>
<br></div><td >String</tr></td></td></td><tr ><td >stand<td ><div>Side of the plate batter is standing.
<br>
<br></div><td >Categorical(ordering='physical')</tr></td></td></td><tr ><td >p_throws<td ><div>Hand pitcher throws with.
<br>
<br></div><td >Categorical(ordering='physical')</tr></td></td></td><tr ><td >home_team<td ><div>Abbreviation of home team.
<br>
<br></div><td >Categorical(ordering='physical')</tr></td></td></td><tr ><td >away_team<td ><div>Abbreviation of away team.
<br>
<br></div><td >Categorical(ordering='physical')</tr></td></td></td><tr ><td >type<td ><div>Short hand of pitch result. B = ball, S = strike, X = in play.
<br>
<br></div><td >Categorical(ordering='physical')</tr></td></td></td><tr ><td >hit_location<td ><div>Position of first fielder to touch the ball.
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >bb_type<td ><div>Batted ball type, ground_ball, line_drive, fly_ball, popup.
<br>
<br></div><td >Categorical(ordering='physical')</tr></td></td></td><tr ><td >balls<td ><div>Pre-pitch number of balls in count.
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >strikes<td ><div>Pre-pitch number of strikes in count.
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >pfx_x<td ><div>Horizontal movement in feet from the catcher's perspective.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >pfx_z<td ><div>Vertical movement in feet from the catcher's perpsective.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >plate_x<td ><div>Horizontal position of the ball when it crosses home plate from the catcher's perspective.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >plate_z<td ><div>Vertical position of the ball when it crosses home plate from the catcher's perspective.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >on_3b<td ><div>Pre-pitch MLB Player Id of Runner on 3B.
<br>
<br></div><td >UInt32</tr></td></td></td><tr ><td >on_2b<td ><div>Pre-pitch MLB Player Id of Runner on 2B.
<br>
<br></div><td >UInt32</tr></td></td></td><tr ><td >on_1b<td ><div>Pre-pitch MLB Player Id of Runner on 1B.
<br>
<br></div><td >UInt32</tr></td></td></td><tr ><td >outs_when_up<td ><div>Pre-pitch number of outs.
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >inning<td ><div>Pre-pitch inning number.
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >inning_topbot<td ><div>Pre-pitch top or bottom of inning.
<br>
<br></div><td >Categorical(ordering='physical')</tr></td></td></td><tr ><td >hc_x<td ><div>Hit coordinate X of batted ball.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >hc_y<td ><div>Hit coordinate Y of batted ball.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >fielder_2<td ><div>MLB Player Id for catcher.
<br>
<br></div><td >UInt32</tr></td></td></td><tr ><td >vx0<td ><div>The velocity of the pitch, in feet per second, in x-dimension, determined at y=50 feet.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >vy0<td ><div>The velocity of the pitch, in feet per second, in y-dimension, determined at y=50 feet.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >vz0<td ><div>The velocity of the pitch, in feet per second, in z-dimension, determined at y=50 feet.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >ax<td ><div>The acceleration of the pitch, in feet per second per second, in x-dimension, determined at y=50 feet.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >ay<td ><div>The acceleration of the pitch, in feet per second per second, in y-dimension, determined at y=50 feet.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >az<td ><div>The acceleration of the pitch, in feet per second per second, in z-dimension, determined at y=50 feet.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >sz_top<td ><div>Top of the batter's strike zone set by the operator when the ball is halfway to the plate.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >sz_bot<td ><div>Bottom of the batter's strike zone set by the operator when the ball is halfway to the plate.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >hit_distance_sc<td ><td >UInt16</tr></td></td></td><tr ><td >launch_speed<td ><div>Exit velocity of the batted ball as tracked by Statcast. For the limited subset of batted balls not tracked directly, estimates are included based on the process described here.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >launch_angle<td ><div>Launch angle of the batted ball as tracked by Statcast. For the limited subset of batted balls not tracked directly, estimates are included based on the process described here.
<br>
<br></div><td >Int8</tr></td></td></td><tr ><td >effective_speed<td ><div>Derived speed based on the the extension of the pitcher's release.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >release_spin_rate<td ><td >UInt16</tr></td></td></td><tr ><td >release_extension<td ><div>Release extension of pitch in feet as tracked by Statcast.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >game_pk<td ><div>Unique Id for Game.
<br>
<br></div><td >UInt32</tr></td></td></td><tr ><td >pitcher_1<td ><td >UInt32</tr></td></td></td><tr ><td >fielder_2_1<td ><td >UInt32</tr></td></td></td><tr ><td >fielder_3<td ><div>MLB Player Id for 1B.
<br>
<br></div><td >UInt32</tr></td></td></td><tr ><td >fielder_4<td ><div>MLB Player Id for 2B.
<br>
<br></div><td >UInt32</tr></td></td></td><tr ><td >fielder_5<td ><div>MLB Player Id for 3B.
<br>
<br></div><td >UInt32</tr></td></td></td><tr ><td >fielder_6<td ><div>MLB Player Id for SS.
<br>
<br></div><td >UInt32</tr></td></td></td><tr ><td >fielder_7<td ><div>MLB Player Id for LF.
<br>
<br></div><td >UInt32</tr></td></td></td><tr ><td >fielder_8<td ><div>MLB Player Id for CF.
<br>
<br></div><td >UInt32</tr></td></td></td><tr ><td >fielder_9<td ><div>MLB Player Id for RF.
<br>
<br></div><td >UInt32</tr></td></td></td><tr ><td >release_pos_y<td ><div>Release position of pitch measured in feet from the catcher's perspective.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >estimated_ba_using_speedangle<td ><div>Estimated Batting Avg based on launch angle and exit velocity.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >estimated_woba_using_speedangle<td ><div>Estimated wOBA based on launch angle and exit velocity.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >woba_value<td ><div>wOBA value based on result of play.
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >woba_denom<td ><div>wOBA denominator based on result of play.
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >babip_value<td ><div>BABIP value based on result of play.
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >iso_value<td ><div>ISO value based on result of play.
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >launch_speed_angle<td ><div>Launch speed/angle zone based on launch angle and exit velocity.
<br>1: Weak
<br>2: Topped
<br>3: Under
<br>4: Flare/Burner
<br>5: Solid Contact
<br>6: Barrel
<br>
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >at_bat_number<td ><div>Plate appearance number of the game.
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >pitch_number<td ><div>Total pitch number of the plate appearance.
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >pitch_name<td ><div>The name of the pitch derived from the Statcast Data.
<br>
<br></div><td >Categorical(ordering='physical')</tr></td></td></td><tr ><td >home_score<td ><div>Pre-pitch home score
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >away_score<td ><div>Pre-pitch away score
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >bat_score<td ><div>Pre-pitch bat team score
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >fld_score<td ><div>Pre-pitch field team score
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >post_away_score<td ><div>Post-pitch away score
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >post_home_score<td ><div>Post-pitch home score
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >post_bat_score<td ><div>Post-pitch bat team score
<br>
<br></div><td >UInt8</tr></td></td></td><tr ><td >post_fld_score<td ><td >UInt8</tr></td></td></td><tr ><td >if_fielding_alignment<td ><div>Infield fielding alignment at the time of the pitch.
<br>
<br></div><td >Categorical(ordering='physical')</tr></td></td></td><tr ><td >of_fielding_alignment<td ><div>Outfield fielding alignment at the time of the pitch.
<br>
<br></div><td >Categorical(ordering='physical')</tr></td></td></td><tr ><td >spin_axis<td ><div>The Spin Axis in the 2D X-Z plane in degrees from 0 to 360, such that 180 represents a pure backspin fastball and 0 degrees represents a pure topspin (12-6) curveball
<br>
<br></div><td >UInt16</tr></td></td></td><tr ><td >delta_home_win_exp<td ><div>The change in Win Expectancy before the Plate Appearance and after the Plate Appearance
<br>
<br></div><td >Float64</tr></td></td></td><tr ><td >delta_run_exp<td ><div>The change in Run Expectancy before the Pitch and after the Pitch<br><td >Float64</tr></td></td></td><tr ><td >bat_speed<td ><td >Float64</tr></td></td></td><tr ><td >swing_length<td ><td >Float64</tr></table>