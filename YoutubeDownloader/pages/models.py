from django.db import models


class Historico(models.Model):
	title = models.CharField(max_length=255)
	url = models.URLField(max_length=1024)
	format = models.CharField(max_length=50, default='mp4')
	created_at = models.DateTimeField(auto_now_add=True)
	# optional: path to downloaded file (if used)
	file_path = models.CharField(max_length=1024, blank=True, null=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f"{self.title} ({self.format})"
