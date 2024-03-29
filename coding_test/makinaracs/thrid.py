"""
증가구간이란 k-1번째 배열원소보다 k번째 배열 원소가 더 큰 경우를 말하고, 1개의 증가구간으로 개수를 셉니다.

만약, array = [103, 101, 103, 103, 101, 102, 100, 100, 101, 104]로 주어질때 [101, 103, 100, 101, 102, 103, 100, 101, 103, 104]로 배치하게되면

증가구간은 [101에서 103], [100에서 101], [101에서 102], [102에서 103], [100에서 101], [101에서 103], [103에서 104]로 최대 7개가 됩니다.

배열 원소의 개수가 100,000이하의 자연수이고, 배열 원소의 크기가 1,000,000 이하의 자연수일때, 배열이 주어질때 적당히 배치한 뒤 증가구간 수의 최대값을 반환하는 함수를 작성해주세요.


"""