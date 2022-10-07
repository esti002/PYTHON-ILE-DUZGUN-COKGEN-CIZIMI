# PYTHON İLE DÜZGÜN ÇOKGEN ÇİZİMİ

## equilateral_polygon_drawer

Bu dosyada yer alan kodlar eşkenar çokgen çizmek için yazılmıştır. Bu dosya aşağıdaki fonksiyonları içerir.

- findPoints
- findEquation
- draw

### Fonksiyonlar Hakkında

- **findPoints**

Bu fonksiyonun temel işlevi parametre olarak alınan ilk nokta koordinatları, çizilecek cismin x düzlemine göre açısı, çokgenin bir kenarının uzunluğu ve çokgenin kenar sayısını kullanarak çokgenin diğer köşe noktalarının konumunu bulur. Ve bu noktaları dizi olarak geri döndürür.

##### Fonksiyonun İşleyişi

![fındPoınts fonksıyonu gorsel](https://github.com/esti002/equilateral_polygon_drawer/blob/main/Pictures/equation.png)

Bize verilmiş olan (x₁,y₁) noktasının koordinatlarını x uzunluğunu ve α açısını kullanarak (x₂,y₂) noktası hesaplanır. Şimdi de bu hesaplamanın hangi yollar kullanılarak yapıldığına bakalım.

b = sinα * x
a = b / tanα 

x₂ = x₁ + a
y₂ = y₁ + b

Formülleri kullanılarak (x₂,y₂) noktası tespit edilir. Bir sonraki nokta tespit edirirken yapılacak işlem yeni noktaya göre yapılacağı için x düzlemine göre α açısıyla hesaplamak yeterli olmayacaktır. Bundan dolayı bir sonraki nokta (son noktanın tespitinde kullanılan açı + çokgenin bir iç açısı) şekinde olmalıdır. Bu yapının da otomatik olarak gerçekleşmesi için formüllerde kullanılan açı (α + çokgenin bir iç açısı * (nokta numarası - 1)) şeklinde yapılabilir. 

Bu fonksiyon sayesinde şu anda eşkenar çokgenimizin köşe noktalarını belirlemiş olduk.

- **findEquation**

Bu fonksiyon parametre olarak aldığı iki nokta arasındaki doğru denklemini geri dödürür.

##### Fonksiyonun İşleyişi

![fındPoınts fonksıyonu gorsel](https://github.com/esti002/equilateral_polygon_drawer/blob/main/Pictures/equation.png)

Parametre olarak fonksiyona (x₁,y₁) ve (x₂,y₂) noktalarını kullanarak d doğrusunun denklemi elde edilir. Bu denklem aşağıdaki gibidir.

y = m * x - m * x₁ + y₁    formülü ile doğrunun denklemi elde edilir. 
Bu denklem incelendiğinde temelde (m * x)'in oluşturduğu değişken ve (- m * x₁ + y₁)'in oluşturduğu iki kısımdan oluşmatadır.
Bundan dolayı fonksiyonun geri dönüş değerlerini en aza indirmek adına m değerini ve elde edilen sabit değerini geri döndürürüz.

- **draw**

Bu fonksiyon *findPoints* ve *findEquation* fonksiyonlarını kullanarak elde edilen verileri kullanarak eşkenar çokgenin çizilmesi için gerekli olan pikselleri tespit edip boyama işlemini yapar.

##### Fonksiyonun İşleyişi

Öncelikle bilgisayara fazladan işlem yaptırmamak için çalişacağımız alanı noktaların yer aldığı aralığı tespit ediyoruz.

Ardından elde ettiğimiz denklemlerin altta kalan kısımlarının mı yoksa üstte kalan kısımlarının mı bizim boyamamız uygun olduğunun kontrolünü doğruyu oluştururken kullandığımız noktalar harici bir noktada yerine koyarak tespit ediyoruz. Bu tespitleri yaparken de aşağıdaki yöntemden faydalanıyoruz.

y₁ > m * x₁ + (sabit) => Nokta doğrunun üstündeki bölgededir.
y₁ = m * x₁ + (sabit) => Nokta doğru üzerindedir.
y₁ < m * x₁ + (sabit) => Nokta doğrunun altındaki bölgededir.

Elde ettiğimiz doğruların hepsi için seçili alandaki noktaların hepsi kontrol edilir. tüm doğruları sağlayan noktalar boyanır.




