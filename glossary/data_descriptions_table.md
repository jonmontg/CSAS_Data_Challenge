<table border=1></th></th></th><tr ><th >column<th >description<th >data_type</tr></td></td></td><tr ><td >pitch_type<td ><span>The type of pitch derived from Statcast.
<br>
<br></span><td >String</tr></td></td></td><tr ><td >game_date<td ><span>Date of the Game.
<br>
<br></span><td >String</tr></td></td></td><tr ><td >release_speed<td ><span>Pitch velocities from 2008-16 are via Pitch F/X, and adjusted to roughly out-of-hand release point. All velocities from 2017 and beyond are Statcast, which are reported out-of-hand.
<br>
<br></span><td >String</tr></td></td></td><tr ><td >release_pos_x<td ><span>Horizontal Release Position of the ball measured in feet from the catcher's perspective.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >release_pos_z<td ><span>Vertical Release Position of the ball measured in feet from the catcher's perspective.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >player_name<td ><span>Player's name tied to the event of the search.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >batter<td ><span>MLB Player Id tied to the play event.
<br>
<br></span><td >String</tr></td></td></td><tr ><td >pitcher<td ><span>MLB Player Id tied to the play event.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >events<td ><span>Event of the resulting Plate Appearance.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >description<td ><span>Description of the resulting pitch.
<br>
<br></span><td >String</tr></td></td></td><tr ><td >spin_dir<td ><span>* Deprecated field from the old tracking system.
<br>
<br></span><td >String</tr></td></td></td><tr ><td >spin_rate_deprecated<td ><span>* Deprecated field from the old tracking system. Replaced by release_spin
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >break_angle_deprecated<td ><span>* Deprecated field from the old tracking system.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >break_length_deprecated<td ><span>* Deprecated field from the old tracking system.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >zone<td ><span>Zone location of the ball when it crosses the plate from the catcher's perspective.
<br>
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >des<td ><span>Plate appearance description from game day.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >game_type<td ><span>Type of Game. E = Exhibition, S = Spring Training, R = Regular Season, F = Wild Card, D = Divisional Series, L = League Championship Series, W = World Series
<br>
<br></span><td >String</tr></td></td></td><tr ><td >stand<td ><span>Side of the plate batter is standing.
<br>
<br></span><td >String</tr></td></td></td><tr ><td >p_throws<td ><span>Hand pitcher throws with.
<br>
<br></span><td >String</tr></td></td></td><tr ><td >home_team<td ><span>Abbreviation of home team.
<br>
<br></span><td >String</tr></td></td></td><tr ><td >away_team<td ><span>Abbreviation of away team.
<br>
<br></span><td >String</tr></td></td></td><tr ><td >type<td ><span>Short hand of pitch result. B = ball, S = strike, X = in play.
<br>
<br></span><td >String</tr></td></td></td><tr ><td >hit_location<td ><span>Position of first fielder to touch the ball.
<br>
<br></span><td >String</tr></td></td></td><tr ><td >bb_type<td ><span>Batted ball type, ground_ball, line_drive, fly_ball, popup.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >balls<td ><span>Pre-pitch number of balls in count.
<br>
<br></span><td >String</tr></td></td></td><tr ><td >strikes<td ><span>Pre-pitch number of strikes in count.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >game_year<td ><span>Year game took place.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >pfx_x<td ><span>Horizontal movement in feet from the catcher's perspective.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >pfx_z<td ><span>Vertical movement in feet from the catcher's perpsective.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >plate_x<td ><span>Horizontal position of the ball when it crosses home plate from the catcher's perspective.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >plate_z<td ><span>Vertical position of the ball when it crosses home plate from the catcher's perspective.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >on_3b<td ><span>Pre-pitch MLB Player Id of Runner on 3B.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >on_2b<td ><span>Pre-pitch MLB Player Id of Runner on 2B.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >on_1b<td ><span>Pre-pitch MLB Player Id of Runner on 1B.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >outs_when_up<td ><span>Pre-pitch number of outs.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >inning<td ><span>Pre-pitch inning number.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >inning_topbot<td ><span>Pre-pitch top or bottom of inning.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >hc_x<td ><span>Hit coordinate X of batted ball.
<br>
<br></span><td >String</tr></td></td></td><tr ><td >hc_y<td ><span>Hit coordinate Y of batted ball.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >tfs_deprecated<td ><span>* Deprecated field from old tracking system.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >tfs_zulu_deprecated<td ><span>* Deprecated field from old tracking system.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >fielder_2<td ><span>Pre-pitch MLB Player Id of Catcher.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >umpire<td ><span>* Deprecated field from old tracking system.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >sv_id<td ><span>Non-unique Id of play event per game.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >vx0<td ><span>The velocity of the pitch, in feet per second, in x-dimension, determined at y=50 feet.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >vy0<td ><span>The velocity of the pitch, in feet per second, in y-dimension, determined at y=50 feet.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >vy0<td ><span>The velocity of the pitch, in feet per second, in z-dimension, determined at y=50 feet.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >ax<td ><span>The acceleration of the pitch, in feet per second per second, in x-dimension, determined at y=50 feet.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >ay<td ><span>The acceleration of the pitch, in feet per second per second, in y-dimension, determined at y=50 feet.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >az<td ><span>The acceleration of the pitch, in feet per second per second, in z-dimension, determined at y=50 feet.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >sz_top<td ><span>Top of the batter's strike zone set by the operator when the ball is halfway to the plate.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >sz_bot<td ><span>Bottom of the batter's strike zone set by the operator when the ball is halfway to the plate.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >hit_distance<td ><span>Projected hit distance of the batted ball.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >launch_speed<td ><span>Exit velocity of the batted ball as tracked by Statcast. For the limited subset of batted balls not tracked directly, estimates are included based on the process described here.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >launch_angle<td ><span>Launch angle of the batted ball as tracked by Statcast. For the limited subset of batted balls not tracked directly, estimates are included based on the process described here.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >effective_speed<td ><span>Derived speed based on the the extension of the pitcher's release.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >release_spin<td ><span>Spin rate of pitch tracked by Statcast.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >release_extension<td ><span>Release extension of pitch in feet as tracked by Statcast.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >game_pk<td ><span>Unique Id for Game.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >pitcher<td ><span>MLB Player Id tied to the play event.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >fielder_2<td ><span>MLB Player Id for catcher.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >fielder_3<td ><span>MLB Player Id for 1B.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >fielder_4<td ><span>MLB Player Id for 2B.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >fielder_5<td ><span>MLB Player Id for 3B.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >fielder_6<td ><span>MLB Player Id for SS.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >fielder_7<td ><span>MLB Player Id for LF.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >fielder_8<td ><span>MLB Player Id for CF.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >fielder_9<td ><span>MLB Player Id for RF.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >release_pos_y<td ><span>Release position of pitch measured in feet from the catcher's perspective.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >estimated_ba_using_speedangle<td ><span>Estimated Batting Avg based on launch angle and exit velocity.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >estimated_woba_using_speedangle<td ><span>Estimated wOBA based on launch angle and exit velocity.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >woba_value<td ><span>wOBA value based on result of play.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >woba_denom<td ><span>wOBA denominator based on result of play.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >babip_value<td ><span>BABIP value based on result of play.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >iso_value<td ><span>ISO value based on result of play.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >launch_speed_angle<td ><span>Launch speed/angle zone based on launch angle and exit velocity.
<br>1: Weak
<br>2: Topped
<br>3: Under
<br>4: Flare/Burner
<br>5: Solid Contact
<br>6: Barrel
<br>
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >at_bat_number<td ><span>Plate appearance number of the game.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >pitch_number<td ><span>Total pitch number of the plate appearance.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >pitch_name<td ><span>The name of the pitch derived from the Statcast Data.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >home_score<td ><span>Pre-pitch home score
<br>
<br></span><td >String</tr></td></td></td><tr ><td >away_score<td ><span>Pre-pitch away score
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >bat_score<td ><span>Pre-pitch bat team score
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >fld_score<td ><span>Pre-pitch field team score
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >post_home_score<td ><span>Post-pitch home score
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >post_away_score<td ><span>Post-pitch away score
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >post_bat_score<td ><span>Post-pitch bat team score
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >if_fielding_alignment<td ><span>Infield fielding alignment at the time of the pitch.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >of_fielding_alignment<td ><span>Outfield fielding alignment at the time of the pitch.
<br>
<br></span><td >Float64</tr></td></td></td><tr ><td >spin_axis<td ><span>The Spin Axis in the 2D X-Z plane in degrees from 0 to 360, such that 180 represents a pure backspin fastball and 0 degrees represents a pure topspin (12-6) curveball
<br>
<br></span><td >String</tr></td></td></td><tr ><td >delta_home_win_exp<td ><span>The change in Win Expectancy before the Plate Appearance and after the Plate Appearance
<br>
<br></span><td >String</tr></table>