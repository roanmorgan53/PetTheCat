extends Node2D

@onready var text_box: RichTextLabel = $RichTextLabel

func _process(delta: float) -> void:
	text_box.text = str(Global.clicks + 1)
