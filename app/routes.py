
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

# class Planet:
#     def __init__(self, id, name, description, color):
#         self.id = id
#         self.name = name 
#         self.description = description
#         self.color = color
    
# def return_planets(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "description": self.description,
#             "color": self.color  
#         }
        

# planets = [
#     Planet(1,"Mercury", "hot", "brown"), 
#     Planet(2, "Venus", "pretty", "redish brown"),
#     Planet(3, "Earth", "wet", "greenis blue"),
#     Planet(6, "Saturn", "rings", "purple and yellow" )

# ]
    

solar_systems_bp = Blueprint("planets", __name__, url_prefix="/planets")


@solar_systems_bp.route("", methods=["POST"])
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        color=request_body["color"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)
# @solar_systems_bp.route("", methods=["GET", "POST"])
# def get_planet_json():
#     planet_response = []
#     for planet in planets:
#         planet_response.append(
#             planet.return_planets()
#         )
#     return jsonify(planet_response)

# @solar_systems_bp.route("/<planet_id>", methods=["GET"])
# def get_each_planet_with_id(planet_id):
#     planet_id = int(planet_id)
    

#     for planet in planets:
#         if planet.id == planet_id:
#             return jsonify(planet.return_planets())

#     return {
#         "error": (f"ID {planet_id} not exists"),
#         "status": "404"
#     },404 


