extends CharacterBody2D

# import both the sprite and the collision box for manipulation
@onready var animated_sprite: AnimatedSprite2D = $AnimatedSprite2D
@onready var collision_area: Area2D = $Area2D

# variables for gameplay
@export var total_clicks: int = 10
@export var current_clicks: int = 0

# process the cat every frame
func _process(float) -> void:
	
	# play the idle animation for now
	if not animated_sprite.is_playing():
		animated_sprite.play("idle")

# process inputs
func _input(event):
	if event is InputEventMouseButton and collision_area.mouse_entered:
		if current_clicks + 1 != total_clicks:
			current_clicks += 1
		else:
			current_clicks = 0
			# update to a different kitty
		print(current_clicks)
