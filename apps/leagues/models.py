from django.db import models

class League(models.Model):
	name = models.CharField(max_length=50)
	sport = models.CharField(max_length=15)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ['name', 'sport']

class Team(models.Model):
	location = models.CharField(max_length=50)
	team_name = models.CharField(max_length=50)
	league = models.ForeignKey(League, related_name="teams")
	class Meta:
		ordering = ['team_name', 'location']

class Player(models.Model):
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	curr_team = models.ForeignKey(Team, related_name="curr_players")
	all_teams = models.ManyToManyField(Team, related_name="all_players")
	class Meta:
		ordering = ['-first_name', 'last_name']
