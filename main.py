
from book import Book
from library import Library # type: ignore

def main():
    library = Library()

    while True:
        print("\n Kütüphane Uygulaması")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Kitap Ara")
        print("5. Çıkış")

        choice = input("Seçiminizi yapın (1-5): ")

        if choice == "1":
            title = input("Kitap adı: ")
            author = input("Yazar: ")
            isbn = input("ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print(" Kitap eklendi!")

        elif choice == "2":
            isbn = input("Silmek istediğiniz kitabın ISBN numarası: ")
            library.remove_book(isbn)
            print(" Kitap silindi (varsa).")

        elif choice == "3":
            print("\n--- Kütüphanedeki Kitaplar ---")
            library.list_books()

        elif choice == "4":
            isbn = input("Aramak istediğiniz kitabın ISBN numarası: ")
            book = library.find_book(isbn)
            if book:
                print(" Bulundu:", book)
            else:
                print("Kitap bulunamadı.")

        elif choice == "5":
            print(" Program sonlandırılıyor...")
            break

        else:
            print(" Geçersiz seçim! Lütfen 1-5 arasında bir değer girin.")

if __name__ == "__main__":
    main()
