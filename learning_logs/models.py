from django.db import models


class Topic(models.Model):
    """A topic the user is learning about."""
    text: models.CharField = models.CharField(max_length=200)
    date_added: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """something specific learned abount a topic."""
    topic: models.ForeignKey = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE)
    text: models.TextField = models.TextField()
    date_added: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta options for the Entry model."""
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text
