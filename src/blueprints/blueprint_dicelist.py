from flask import Blueprint, jsonify, request, session

blueprint_dicelist = Blueprint(name="blueprint_dicelist", import_name=__name__)




@blueprint_dicelist.route('/test', methods=['GET'])
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
              schema: OutputSchema
      tags:
          - testing
    """
    output = {"msg": "I'm the test endpoint from blueprint_dicelist."}
    return jsonify(output)


@blueprint_dicelist.route('/dicelist', methods=['GET'])
def viewList():
    """
    ---
    get:
      description: get past results list
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchemaList
      tags:
          - result list
    """
    if 'throws' in session:
      output = {"list": "your last results are '{}'"}
      return jsonify('list',session['throws'])
    else:
      return jsonify('msg', 'Please Throw a Dice or activate cookies')
    
