PROBLEM 1:
Task 1:
    - The shape of the DataFrame is (150, 5), it means there are 150 rows and 5 columns
    - The data type of each column:
        sepal_length    float64
        sepal_width     float64
        petal_length    float64
        petal_width     float64
        species             str
Task 3: Alnalyze each group of species
    Consider to the mean of each feature, especially petal_lenght and petal_width, the pair of Setosa and Virginica has the most difference. Moreover, their standard deviation are quite small compared to the distance between their mean. It means that the figure of these species are seperated well.

PROBLEM 2:
Task 1:
    ![alt text](Histogram_KDE_All.png)
    Look at the figure, we can easily claim that:
    - sepal_length and sepal_width distributions are unimodal. Both of them are similar to normal distribution. Moreover, the distribution of sepal_length is slightly right-skewed because a few observations have relatively large values (up to about 8 cm)
    - petal_length and petal_width distributions are significantly bimodal. Explaining for this problem, please look at the below figure
    ![alt text](Histogram_KDE_Petal.png)
    - When we plot petal_lendth and petal_width for each species, each feature of each species also has an approximately standard distribution. However, these figure of each species is dinstinct from one another, then when we plot the whole feature, its distribution will not standard. With this detail, we can easily define each species by petal_lendth or petal_width.

Task 2:
    ![alt text](Boxplot.png)
    Virginica generally has larger measurements than Versicolor across all four features.
    Setosa has the largest sepal width. However, for the other three features (sepal length, petal length, and petal width), it has the smallest measurements among the three species.

Task 3:
    I choose sepal_width to compare with PDF theoretical
    ![alt text](Sepalwidth_PDF.png)
    As shown in the figure, the histogram and the theoretical Normal PDF have a similar bell-shaped pattern and peak near the same mean value. Although there are slight deviations, especially in the tails, the theoretical PDF fits the observed data reasonably well.


PROBLEM 3:
Task 2:
    ![alt text](Heatmap.png)
    The heatmap shows that petal_length and petal_width have the strongest positive correlation (r = 0.963). This indicates that flowers with longer petals generally also have wider petals. Since the correlation coefficient is very close to 1, these two variables show a strong indication of multicollinearity.
Task 3:
    ![alt text](Pairplot.png)
    The pairplot reveals several relationships among the four features. Petal length and petal width have the strongest positive linear relationship, indicating that flowers with longer petals generally have wider petals. Sepal length is also positively correlated with both petal features, whereas sepal width shows a weak negative correlation with them.
    Regarding species separation, Setosa forms a clearly distinct cluster, especially in the petal-related plots. Versicolor and Virginica overlap slightly, particularly in the sepal features, but are better separated by petal length and petal width. Therefore, the petal features are the most informative variables for distinguishing Iris species.

PROBLEM 4:
Task 2:
    Theo em hiểu tính "phản trực giác" mà câu hỏi đề cập là nghịch lý vì sao độ chính xác của test tức là P(+|B) cao nhưng khi tỉ lệ bệnh tức P(B) thấp thì xác suất mắc bệnh khi test dương tính tức P(B|+) lại thấp. Đáng lí ra khi số người mắc bệnh ít và độ chính xác test cao thì test này phải phát hiện chính xác người bệnh hơn. Điều "phản trực giác" được lí giải do khi tỉ lệ bệnh thấp tức số người không mắc bệnh rất nhiều. Từ đó khi lượng người không mắc bệnh đủ nhiều thì số lượng người dương tính giả cũng sẽ rất lớn và có thể áp đảo số người dương tính thật. Vì thế mà dù cho độ chính xác cao nhưng tỉ lệ bệnh thấp thì kết quả test dương tính cũng không đáng tin cậy, cần phải test thêm nhiều lần nữa.