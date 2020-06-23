from score import Score

def key_avg(item):
    return item[1].avg
    
class ScoreManagementSystem:
    def __init__(self):
        self._scores = {}

    def read(self, score_data_file):
        self._scores = {}
        with open(score_data_file, 'rt', encoding = 'utf-8') as fo:
            data = fo.read()
            lines = data.strip().split('\n')

        num = 0
        for line in lines:
            num = num + 1
            self._scores[num] = Score(line.strip())

        return len(self._scores)

    def _make_scores_string(self, scores):
        result=""
        for key, item in scores:
            result = result + str(key) + ","
            result = result + item.sid + ","
            result = result + item.name + ","
            result = result + str(int(item.kor)) + ","
            result = result + str(int(item.eng)) + ","
            result = result + str(int(item.math)) + ","
            result = result + str(int(item.total)) + ","
            result = result + str(int(item.avg)) + "\n"
        return result.strip()

    def sort(self, order_key="register", order_way="asc"):
        if order_key == "register" and order_way == "asc":
            sorted_scores = sorted(self._scores.items())
        elif order_key =="register" and order_way == "des":
            sorted_scores = sorted(self._scores.items(), reverse=True)
        elif order_key == "avg" and order_way == "asc":
            sorted_scores = sorted(self._scores.items(), key=key_avg)
        elif order_key == "avg" and order_way == "des":
            sorted_scores = sorted(self._scores.items(), key=key_avg, reverse=True)

        result = self._make_scores_string(sorted_scores)
        return result

    def write(self, file_name, order_key="register", order_way="asc"):
        with open(file_name, 'wt', encoding='utf-8') as fo:
            result = self.sort(order_key, order_way)
            fo.write(result)