from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('matches-per-year',views.match_per_year_all_years,name='matches-per-year'),
    path('won-per-year-per-team',views.won_per_team_per_year,name='won-per-year-per-team'),
    path('extra-runs-conceded',views.extra_runs_conceded,name='extra-runs-conceded'),
    path('top-ten-economical-bowlers',views.top_ten_economical_bowlers,name='top-ten-economical-bowlers'),
    path('match-per-year/chart',views.match_per_year_chart,name='match-per-year-chart'),
    path('won-per-year-per-team/chart',views.won_per_year_chart,name='won-per-year-per-team-chart'),
    path('extra-runs-conceded/chart',views.extra_runs_conceded_chart,name='extra-runs-conceded-chart'),
    path('top-ten-economical-bowlers/chart',views.top_ten_economical_bowlers_chart,name='top-ten-economical-bowlers-chart')
]