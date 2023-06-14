from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader,Context
from . models import Matches, Deliveries
from django.http import JsonResponse
from django.db.models import Count,Sum
from django.core import serializers
#from . import Deliveries, Matches

# Create your views here.
def index(request):
    template=loader.get_template('stats/index.html')
    answer=Matches.objects.count()
    delivery=Deliveries.objects.count()
    return HttpResponse(template.render({"match":answer,"delivery":delivery},request))

def match_per_year_all_years(request):
    answer=list(Matches.objects.values('season').annotate(count=Count('season')))
    return JsonResponse(answer,safe=False)

def won_per_team_per_year(request):
    answer=list(Matches.objects.exclude(winner="").values('winner','season').annotate(win_count=Count('winner')).order_by('season'))
    return JsonResponse(answer,safe=False)

def extra_runs_conceded(request):
    answer=list(Deliveries.objects.filter(match_id__season="2016").values("bowling_team").annotate(Runs=Sum('extra_runs'))) #
    return JsonResponse(answer,safe=False)

def top_ten_economical_bowlers(request):
    answer=list(Deliveries.objects.filter(match_id__season="2015").values("bowler").annotate(economy=Sum('total_runs')*6/Count('total_runs')).order_by("economy"))[:10]
    return JsonResponse(answer,safe=False)

def match_per_year_chart(request):
    template=loader.get_template('stats/matches-per-year.html')
    return HttpResponse(template.render({},request))

def won_per_year_chart(request):
    template=loader.get_template('stats/won-per-team-per-year.html')
    return HttpResponse(template.render({},request))

def extra_runs_conceded_chart(request):
    template=loader.get_template('stats/extra-runs-conceded.html')
    return HttpResponse(template.render({},request))

def top_ten_economical_bowlers_chart(request):
    template=loader.get_template('stats/top-ten-economical-bowlers.html')
    return HttpResponse(template.render({},request))