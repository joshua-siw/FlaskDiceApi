from flask import Blueprint, jsonify, request,session
from random import randint
from .metrics import throws_metric, results_metric


blueprint_dice = Blueprint(name="blueprint_dice", import_name=__name__)

# Erstelle den Würfel 
def dice():
  result = randint(1,6)
  return result

# Erstellt oder fügt zur Session hinzu
def checksession(keystr,result):
  if keystr in session:
    session[keystr].append(result)
  else:
    session[keystr] = [result]
    
@blueprint_dice.route('/dice/test', methods=['GET'])
def test():
    """
    ---
    get:
      description: test endpoint
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchemaResult
      tags:
          - testing
    """
    output = {"msg": "I'm the test endpoint from blueprint_dice."}
    return jsonify(output)


@blueprint_dice.route('/dice', methods=['GET'])
def rolldice():
    """
    ---
    get:
      description: get dice result
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchemaResult
      tags:
          - result
    """
    throws_metric.inc()
    diceRes = dice()
    checksession("throws",diceRes)
    results_metric.observe(diceRes)
    output = {"msg": f"Your result is: '{diceRes}'"}
    return jsonify('number',diceRes) 

