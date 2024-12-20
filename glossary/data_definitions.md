[source](https://baseballsavant.mlb.com/csv-docs)

### pitch_type
The type of pitch derived from Statcast.

### game_date
Date of the Game.

### release_speed
Pitch velocities from 2008-16 are via Pitch F/X, and adjusted to roughly out-of-hand release point. All velocities from 2017 and beyond are Statcast, which are reported out-of-hand.

### release_pos_x
Horizontal Release Position of the ball measured in feet from the catcher's perspective.

### release_pos_z
Vertical Release Position of the ball measured in feet from the catcher's perspective.

### player_name
Player's name tied to the event of the search.

### batter
MLB Player Id tied to the play event.

### pitcher
MLB Player Id tied to the play event.

### events
Event of the resulting Plate Appearance.

### description
Description of the resulting pitch.

### spin_dir
* Deprecated field from the old tracking system.

### spin_rate_deprecated
* Deprecated field from the old tracking system. Replaced by release_spin

### break_angle_deprecated
* Deprecated field from the old tracking system.

### break_length_deprecated
* Deprecated field from the old tracking system.

### zone
Zone location of the ball when it crosses the plate from the catcher's perspective.


### des
Plate appearance description from game day.

### game_type
Type of Game. E = Exhibition, S = Spring Training, R = Regular Season, F = Wild Card, D = Divisional Series, L = League Championship Series, W = World Series

### stand
Side of the plate batter is standing.

### p_throws
Hand pitcher throws with.

### home_team
Abbreviation of home team.

### away_team
Abbreviation of away team.

### type
Short hand of pitch result. B = ball, S = strike, X = in play.

### hit_location
Position of first fielder to touch the ball.

### bb_type
Batted ball type, ground_ball, line_drive, fly_ball, popup.

### balls
Pre-pitch number of balls in count.

### strikes
Pre-pitch number of strikes in count.

### game_year
Year game took place.

### pfx_x
Horizontal movement in feet from the catcher's perspective.

### pfx_z
Vertical movement in feet from the catcher's perpsective.

### plate_x
Horizontal position of the ball when it crosses home plate from the catcher's perspective.

### plate_z
Vertical position of the ball when it crosses home plate from the catcher's perspective.

### on_3b
Pre-pitch MLB Player Id of Runner on 3B.

### on_2b
Pre-pitch MLB Player Id of Runner on 2B.

### on_1b
Pre-pitch MLB Player Id of Runner on 1B.

### outs_when_up
Pre-pitch number of outs.

### inning
Pre-pitch inning number.

### inning_topbot
Pre-pitch top or bottom of inning.

### hc_x
Hit coordinate X of batted ball.

### hc_y
Hit coordinate Y of batted ball.

### tfs_deprecated
* Deprecated field from old tracking system.

### tfs_zulu_deprecated
* Deprecated field from old tracking system.

### fielder_2
Pre-pitch MLB Player Id of Catcher.

### umpire
* Deprecated field from old tracking system.

### sv_id
Non-unique Id of play event per game.

### vx0
The velocity of the pitch, in feet per second, in x-dimension, determined at y=50 feet.

### vy0
The velocity of the pitch, in feet per second, in y-dimension, determined at y=50 feet.

### vz0
The velocity of the pitch, in feet per second, in z-dimension, determined at y=50 feet.

### ax
The acceleration of the pitch, in feet per second per second, in x-dimension, determined at y=50 feet.

### ay
The acceleration of the pitch, in feet per second per second, in y-dimension, determined at y=50 feet.

### az
The acceleration of the pitch, in feet per second per second, in z-dimension, determined at y=50 feet.

### sz_top
Top of the batter's strike zone set by the operator when the ball is halfway to the plate.

### sz_bot
Bottom of the batter's strike zone set by the operator when the ball is halfway to the plate.

### hit_distance
Projected hit distance of the batted ball.

### launch_speed
Exit velocity of the batted ball as tracked by Statcast. For the limited subset of batted balls not tracked directly, estimates are included based on the process described here.

### launch_angle
Launch angle of the batted ball as tracked by Statcast. For the limited subset of batted balls not tracked directly, estimates are included based on the process described here.

### effective_speed
Derived speed based on the the extension of the pitcher's release.

### release_spin
Spin rate of pitch tracked by Statcast.

### release_extension
Release extension of pitch in feet as tracked by Statcast.

### game_pk
Unique Id for Game.

### pitcher
MLB Player Id tied to the play event.

### fielder_2
MLB Player Id for catcher.

### fielder_3
MLB Player Id for 1B.

### fielder_4
MLB Player Id for 2B.

### fielder_5
MLB Player Id for 3B.

### fielder_6
MLB Player Id for SS.

### fielder_7
MLB Player Id for LF.

### fielder_8
MLB Player Id for CF.

### fielder_9
MLB Player Id for RF.

### release_pos_y
Release position of pitch measured in feet from the catcher's perspective.

### estimated_ba_using_speedangle
Estimated Batting Avg based on launch angle and exit velocity.

### estimated_woba_using_speedangle
Estimated wOBA based on launch angle and exit velocity.

### woba_value
wOBA value based on result of play.

### woba_denom
wOBA denominator based on result of play.

### babip_value
BABIP value based on result of play.

### iso_value
ISO value based on result of play.

### launch_speed_angle
Launch speed/angle zone based on launch angle and exit velocity.
1: Weak
2: Topped
3: Under
4: Flare/Burner
5: Solid Contact
6: Barrel


### at_bat_number
Plate appearance number of the game.

### pitch_number
Total pitch number of the plate appearance.

### pitch_name
The name of the pitch derived from the Statcast Data.

### home_score
Pre-pitch home score

### away_score
Pre-pitch away score

### bat_score
Pre-pitch bat team score

### fld_score
Pre-pitch field team score

### post_home_score
Post-pitch home score

### post_away_score
Post-pitch away score

### post_bat_score
Post-pitch bat team score

### if_fielding_alignment
Infield fielding alignment at the time of the pitch.

### of_fielding_alignment
Outfield fielding alignment at the time of the pitch.

### spin_axis
The Spin Axis in the 2D X-Z plane in degrees from 0 to 360, such that 180 represents a pure backspin fastball and 0 degrees represents a pure topspin (12-6) curveball

### delta_home_win_exp
The change in Win Expectancy before the Plate Appearance and after the Plate Appearance

### delta_run_exp
The change in Run Expectancy before the Pitch and after the Pitch

### swing_length
The total (sum) distance in feet traveled of the head of the bat in X/Y/Z space, from start of tracking data until impact point.

### bat_speed
Bat speed is measured at the sweet-spot of the bat. Average bat speed is the average of the top 90% of a player’s swings.