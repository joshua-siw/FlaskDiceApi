from flask import Blueprint
from prometheus_client import Counter, Summary

throws_metric = Counter('count_throws', 'counts how often dice is rolled')
results_metric = Summary('show_results', 'shows dice throw results')
