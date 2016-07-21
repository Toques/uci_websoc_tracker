from celery import Celery
from celery.utils.log import get_task_logger

from uci_tracker.courses.utils import request_websoc, save_course_data
from uci_tracker.courses.models import Course

logger = get_task_logger(__name__)

app = Celery('tasks',backend='rpc://', broker='amqp://')


@app.task(name = 'uci_tracker.tasks.refresh')
def refresh_data(course_pk):
    course = Course.objects.get(pk = course_pk)
    kwargs = {'YearTerm': '2016-14'}
    info = request_websoc(course.course_code, **kwargs)
    save_course_data(course, info)