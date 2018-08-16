from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# 投票系统
# 根据发布日期显示最近的5个投票问卷
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    content = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', content)


# 返回具体问卷文本内容
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# 投票
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 发生choice未找到异常时，重新返回表单页面，并给出提示信息
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 成功处理数据后，自动跳转到结果页面，防止用户连续多次提交。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
