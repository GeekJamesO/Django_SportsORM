from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		# "leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		'all_baseball_leagues' : League.objects.filter(sport='Baseball'),
		'all_womens_leagues' : League.objects.filter(name__icontains="womens"),
		'all_leagues_where_sport_is_any_type_of_hockey' : League.objects.filter(sport__icontains="hockey"),
		'all_leagues_where_sport_is_something_OTHER_THAN_football' : League.objects.exclude(sport__icontains="football"),
		'all_leagues_that_call_themselves_conferences' : League.objects.filter(name__icontains="conference"),
		'all_leagues_in_the_Atlantic_region' : League.objects.filter(name__icontains="atlantic"),

		'all_teams_based_in_Dallas' : Team.objects.filter(location="Dallas"),
		'all_teams_named_the_Raptors' : Team.objects.filter(team_name__icontains="Raptors"),
		'all_teams_whose_location_includes_City' : Team.objects.filter(location__contains="City"),
		'all_teams_whose_names_begin_with_T' : Team.objects.filter(team_name__startswith="T"),
		'all_teams_ordered_alphabetically_by_location' : Team.objects.order_by('location'),
		'all_teams_ordered_by_team_name_in_reverse_alphabetical_order' : Team.objects.order_by('-team_name'),

		'every_player_with_last_name_Cooper' : Player.objects.filter(last_name="Cooper"),
		'every_player_with_first_name_Joshua' : Player.objects.filter(first_name="Joshua"),
		'every_player_with_last_name_Cooper_EXCEPT_those_with_Joshua_as_the_first_name' : Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		'all_players_with_first_name_Alexander_OR_first_name_Wyatt' : Player.objects.filter(first_name__in=['Alexander', 'Wyatt' ]),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
