from django.test import TestCase

import datetime
from django.utils import timezone
from .models import Question

from django.test import TestCase


# 整个测试用例基本上和Python内置的unittest单元测试非常相似
class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        在将来发布的问卷应该返回False
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
