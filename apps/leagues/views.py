from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index_old(request):
	context = {
		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		# "players": Player.objects.all(),
		'all_baseball_leagues' : League.objects.filter(sport='Baseball'),
		'all_womens_leagues' : League.objects.filter(name__icontains="womens"),
		'all_leagues_where_sport_is_any_type_of_hockey' : League.objects.filter(sport__icontains="hockey"),
		'all_leagues_where_sport_is_something_OTHER_THAN_football' : League.objects.exclude(sport__icontains="football"),
		'all_leagues_that_call_themselves_conferences' : League.objects.filter(name__icontains="conference"),
		'all_leagues_in_the_Atlantic_region' : League.objects.filter(name__icontains="atlantic"),

		'all_teams_based_in_Dallas' : Team.objects.filter(location="Dallas"),
		'all_teams_named_the_Raptors' : Team.objects.filter(team_name__icontains="Raptors"),
		'all_teams_whose_location_includes_City' : Team.objects.filter(location__contains="City"),
		'all_teams_whose_location_includes_City' : Team.objects.filter(team_name__startswith="T"),
		'all_teams_ordered_alphabetically_by_location' : Team.objects.order_by('location'),
		'all_teams_ordered_by_team_name_in_reverse_alphabetical_order' : Team.objects.order_by('-team_name'),

		'every_player_with_last_name_Cooper' : Player.objects.filter(last_name="Cooper"),
		'every_player_with_first_name_Joshua' : Player.objects.filter(first_name="Joshua"),
		'every_player_with_last_name_Cooper_EXCEPT_those_with_Joshua_as_the_first_name' : Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		'all_players_with_first_name_Alexander_OR_first_name_Wyatt' : Player.objects.filter(first_name__in=['Alexander', 'Wyatt' ]),
	}
	return render(request, "leagues/index_old.html", context)

def index_new(request):
	# footballTeamsIds = Team.objects.filter(league__sport="Football").all()
	# print "footballTeamsIds", footballTeamsIds
	context = {
		# "leagues": League.objects.all(),
		'teamsInAtlanticSoccerConference' : League.objects.get(name = "Atlantic Soccer Conference").teams.all(),
		'currentPlayersOnBostonPenguins' : Player.objects.filter(curr_team__team_name__icontains="penguins").filter(curr_team__location = "Boston"),
		'allCurrentPlayersInInternationalCollegiateBaseballConference' : Player.objects.filter(curr_team__league__name = "International Collegiate Baseball Conference"),
		'currentPlayersInTheAmericanConferenceOfAmateurFootballWithLastNameOfLopez' : Player.objects.filter(curr_team__league__name = "American Conference of Amateur Football").filter(last_name = "Lopez"),
		'allFootballPlayersForAllTime' : Player.objects.filter(all_teams__league__sport = "Football").distinct(),
		'teamsWithCurrentPlayerNamedSophia' : Team.objects.filter(all_players__first_name='Sophia'),
		'LeaguesWithCurrentPlayerNamedSophia' : League.objects.filter(teams__all_players__first_name='Sophia'),
		'PlayerNamedFloresNotOnRoughriders' : (Player.objects.filter(first_name='Flores') or Player.objects.filter(last_name='Flores')).exclude(curr_team__team_name='Roughriders') ,
		'TeamsSamuelEvensPlayedOn' : Team.objects.filter(all_players__first_name = 'Samuel').filter(all_players__last_name='Evans'),
		'ManitobaTigerCats_Alumni' : Player.objects.filter(all_teams__team_name="Tiger-Cats").filter(all_teams__location = 'Manitoba'),

		'former_Wichita_Vikings' : Player.objects.exclude(curr_team__team_name="Vikings").filter(all_teams__team_name="Vikings")  # needs more.. need to put merge and case here..

		# ...every team that Jacob Gray played for before he joined the Oregon Colts
		# ...everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
		# ...all teams that have had 12 or more players, past and present. (HINT: Look up the Django annotate function.)
		# ...all players and count of teams played for, sorted by the number of teams they've played for
	}
	return render(request, "leagues/index_new.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
