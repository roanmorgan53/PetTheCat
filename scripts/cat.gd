extends CharacterBody2D

# import both the sprite and the collision box for manipulation
@onready var animated_sprite: AnimatedSprite2D = $AnimatedSprite2D
@onready var collision_area: CollisionShape2D = $CollisionShape2D

# variables for gameplay
@export var max_clicks: int = INF

# process the cat every frame
func _process(float) -> void:
	
	# play the idle animation for now
	if not animated_sprite.is_playing():
		animated_sprite.play("idle")

# process inputs
func _input(event):
	if event is InputEventMouseButton and event.is_action_released("click"):
		if Global.clicks + 1 != max_clicks:
			Global.clicks += 1
		else:
			Global.clicks = 0
			# update to a different kitty
		print(Global.clicks)
