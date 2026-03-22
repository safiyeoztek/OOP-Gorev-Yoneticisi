# Kalıcı Görev Yöneticisi
### Bu uygulama, verileri sadece çalışma anında tutmakla kalmaz, bir metin dosyasına (tasks.txt) kaydederek program kapatılsa bile görevlerin saklanmasını sağlar. Proje, Nesne Yönelimli Programlama (OOP) prensipleri kullanılarak modüler bir yapıda inşa edilmiştir.

## Ne Yapıyor?
* Veri Kalıcılığı: Program başladığında tasks.txt dosyasındaki eski görevleri otomatik yükler.

* Nesne Tabanlı Yapı: Tüm görev yönetimi işlemlerini tek bir TaskManager sınıfı altında toplar.

* Otomatik Kayıt: Kullanıcı çıkış yaparken mevcut görev listesini dosyaya yazarak günceller.

* Hatasız Okuma: encoding="utf-8" kullanarak Türkçe karakter sorunlarını önler.

## Hangi Konular Var?
* Object-Oriented Programming (OOP): class, self ve __init__ (constructor) yapılarının kullanımı.

* File I/O (Dosya İşlemleri): Dosya okuma (r) ve yazma (w) modları ile veri yönetimi.

* Context Managers: with open(...) bloğu ile güvenli dosya yönetimi.

* Metotlar: Sınıf içi fonksiyonlar (Methods) ile görev ekleme, listeleme ve yükleme süreçleri.

## Nasıl Çalıştırılır?
* Bilgisayarınızda Python yüklü olduğundan emin olun.

* Proje klasöründe tasks.txt adında boş bir dosya oluşturun (veya programın ilk kayıtta oluşturmasını bekleyin).

* Terminalden şu komutu çalıştırın:

```Bash
python task_manager_v2.py

```
* Eklediğiniz görevlerin programı kapatıp açtıktan sonra hala orada olduğunu gözlemleyin!
