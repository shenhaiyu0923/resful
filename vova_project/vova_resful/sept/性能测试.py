from locust import HttpLocust, TaskSet, task
# HttpLocust ��������������������http�����
# TaskSet   ������Ƕ����û���Ϊ�ģ��൱��loadrunnerhttpЭ��Ľű���jmeter�����http����һ����Ҫȥ�����
# task   ���task��һ��װ��������������һ��������װ�γ�һ������Ҳ����ָ�����ǵ��Ⱥ�ִ��˳��
class BestTest(TaskSet):
    # �Լ�������࣬�̳�TaskSet��Ҳ�����������ʵ������Ҫȥ����ʲô��
    @task  # ��taskװ�������������װ�γ�һ������Ҫִ�е���������
    def index(self):  # ����������涨���������Ҫ�������Ĳ���
        self.client.get('/')  # �������url������ĸ�·��������ǽӿڵĻ��������ĸ��ӿ�
class BestTestIndexUser(HttpLocust):
    # �����̳���HttpLocust������ÿ�����������ÿ���û�
    task_set = BestTest  # �����ÿ���û���ȥ��ʲô��ָ����BestTest����࣬���ͻ�ÿ���û�ȥ����besttest���������ķ���

    #locust -f ���ܲ���.py --host=http://www.baidu.com
    #localhost��8089

