yellow_pages = {
    '773110' : {
        'family_name' : 'Ariel', 
        'address' : 'Jl. Cepu Ranta',
        'telpon_number' : '773110', 
        'city' : 'Aceh',
        'code_area' : '0651'},
    '6471110' : {
        'family_name' : 'Wardana', 
        'address' : 'Jl. Imam Bonjol',
        'telpon_number' : '6471110', 
        'city' : 'Denpasar',
        'code_area' : '0361'},
    '322333' : {
        'family_name' : 'Salim', 
        'address' : 'Jl. Gatot Subroto',
        'telpon_number' : '322333', 
        'city' : 'Jakarta',
        'code_area' : '021'},
    '421666' : {
        'family_name' : 'Dhika', 
        'address' : 'Jl. Malioboro',
        'telpon_number' : '421666', 
        'city' : 'Jogja',
        'code_area' : '0274'},
    '2390225' : {
        'family_name' : 'Angel', 
        'address' : 'Jl. Jendral Sudirman',
        'telpon_number' : '2390225', 
        'city' : 'Bandung',
        'code_area' : '022'},
}

line = '--------------------------------------------------------------------------------------------------------------------------'
line2 = '==============================================================================================='

# import warna dan pemutar suara
from colorama import Fore
from colorama import Style
from playsound import playsound 

def e_main_menu () :
    print (f'''{Fore.YELLOW}{line2}
            SELAMAT DATANG DI YELLOW PAGES 
{line2}{Style.RESET_ALL}\n
    List Menu :
        1. Menampilkan Daftar Yellow Pages 
        2. Menambah Data Yellow Pages
        3. Mengubah Data Yellow Pages
        4. Menghapus Data Yellow Pages
        5. Hentikan Sistem \n ''')
    playsound('song 1.mp3')
    pilihan_Menu = input ('Masukkan angka Menu yang ingin dijalankan : ')
    if pilihan_Menu == '1' :
        a_menu_read_data ()
    elif pilihan_Menu == '2' :
        b_menu_create_data ()
    elif pilihan_Menu == '3' :
        c_menu_update_data ()
    elif pilihan_Menu == '4' :
        d_menu_delete_data ()
    elif pilihan_Menu == '5' :
        menu_break ()
    else :
        print (f'{line2}\nPilihan yang anda masukkan salah\nMasukkan ulang angka !!!\nTekan Enter Untuk Kembali\n') 
        input ()
        e_main_menu ()


def a_menu_read_data () :
    print (f'''{Fore.GREEN}{line2}
        MENU MENAMPILKAN DAFTAR YELLOW PAGES
{line2}{Style.RESET_ALL}\n
    List Menu :
        1. Menampilkan Semua Data
        2. Mencari Data dari Nomor Telepon
        3. Kembali ke Menu Utama 
        ''')
    playsound('song 2.mp3')
    pilihan_menu_read_data = input ('Masukkan angka Menu yang ingin dijalankan : ')
    #opsi pilihan angka
    if pilihan_menu_read_data == '1' :
        # memakai len untuk mengecek kosong atau tidak daftar yellow pages
        if len(yellow_pages) != 0 :
            show_all_data ()
            print ("\n Klick 'Enter' untuk kembali ke Menu Menampilkan Daftar Yellow Pages  : ")
            input()
            a_menu_read_data ()
        else : 
            print ('Tidak Ada Data Yang Tersimpan \n Ketik Apa Saja untuk kembali ke Menu Menampilkan Daftar Yellow Pages  : ')
            input()
            a_menu_read_data ()
    elif pilihan_menu_read_data == '2' :
        # check memakai len lagi untuk melanjutkan ke find data
        if len(yellow_pages) != 0 :
            find_data_number ()
            
        else : 
            print ('''
            !!! Tidak Ada Data Yang Tersimpan !!!
            Silahkan Tambahkan Data Baru Terlebih Dahulu ! 
            ''')
            a_menu_read_data ()
    elif pilihan_menu_read_data == '3' :
        e_main_menu ()
    else :
        print (f'{line2}\nMASUKKAN OPSI ANGKA YANG BENAR !!!\nKlick Enter untuk kembali ke Menu Menampilkan Daftar Yellow Pages')
        input()
        a_menu_read_data ()
        
def show_all_data () :
    # print judul kolom
    print (f''' \n{line2} \n \n                                   YELLOW PAGES \n        
{'Nama Keluarga':<25}| {'Alamat':<40}| {'No Telepon':<12}| {'Kota':<20}| {'Kode Area':<10}\n{line}''')
    # perulangan for untuk menunjukan semua data 
    for key, val in yellow_pages.items():
        print (f'{yellow_pages[key]["family_name"]:<25}| {yellow_pages[key]["address"]:<40}| {yellow_pages[key]["telpon_number"]:<12}| {yellow_pages[key]["city"]:<20}| {yellow_pages[key]["code_area"]:<10}\n{line}')
    
def find_data_number () :
    print(' ')
    input_find_data_number = input ('Masukkan Nomor yang Ingin Dicari : ')
    # print judul kolom
    print (f''' \n{line2} \n \n                                   YELLOW PAGES \n        
{'Nama Keluarga':<25}| {'Alamat':<40}| {'No Telepon':<12}| {'Kota':<20}| {'Kode Area':<10}''')
    print (line)
    # kondisional jika kolom di dalam yellow pages, jika nomor telpon ada di dalam data
    if input_find_data_number in yellow_pages :
        print (f'{yellow_pages[input_find_data_number]["family_name"]:<25}| {yellow_pages[input_find_data_number]["address"]:<40}| {yellow_pages[input_find_data_number]["telpon_number"]:<12}| {yellow_pages[input_find_data_number]["city"]:<20}| {yellow_pages[input_find_data_number]["code_area"]:<10}\n{line}')
        print (f'\n Klick Enter untuk kembali ke halaman Menampilkan Daftar Yellow Pages \n {line2}')
        input()
        a_menu_read_data ()
    else : 
        input (f'\n NOMOR TELPON TIDAK ADA DI YELLOW PAGES \n \n Klick Enter untuk kembali ke Menu Menampilkan Daftar Yellow Pages \n \n {line2}')
        a_menu_read_data ()
        

def b_menu_create_data () :
    print (f'''{Fore.BLUE}{line2}
        MENU MENAMBAH DAFTAR YELLOW PAGES\n{line2}{Style.RESET_ALL}\n
    List Menu :
        1. Menambahkan Data
        2. Kembali ke Menu Utama\n
        ''')
    playsound('song 3.mp3')
    pilihan_menu_create_data = input ('Masukkan angka menu yang ingin dijalankan : ')
    # kondisional opsi pilihan angka
    if pilihan_menu_create_data == '1' :
        print (f'{line2}\nSilahkan Masukkan Data Nomor Telepon yang Ingin Ditambahkan\n' )
        # input data nomor telpon
        input_cd_telpon_number = input ('Masukkan Nomor Telpon  : ' )
        # jika input nomor telpon ada atau tidak di dalam data
        if input_cd_telpon_number in yellow_pages :
            input (f'{line2}\n\n!!! Data Sudah Ada di Yellow Pages !!!\nTekan Enter untuk kembali ke MENU MENAMBAH DAFTAR YELLOW PAGES\n')
            b_menu_create_data ()
        # jika input ada dalam data dan input data nomor telpon adalah string angka
        # akan membuat val masing" key dan sebagian data akan dibuah capital setiap huruf depannya 
        elif input_cd_telpon_number not in yellow_pages and input_cd_telpon_number.isdigit() :
            print ('Silahkan Masukkan Kelengkapan Data di Yellow Pages\n')
            input_cd_family_name = input ('Nama Keluarga : ' ).title()
            input_cd_address = input ('Alamat : ' ).title()
            input_cd_city = input ('Kota : ' ).title()
            input_cd_code_area = input ('Kode Area : ' )
            # jika input kode area yg dimasukkan bukan angka
            # maka akan melakukan perulangan untuk input kembali
            while True :
                if not input_cd_code_area.isdigit () :
                    print ('\n!!! TIPE DATA YANG ANDA MASUKKAN SALAH !!!\nMasukkan kembali kode area yang benar !\n')
                    input_cd_code_area = input ('Kode Area : ' )
                else : 
                    break
            # menunjukan data baru yg sudah di input 
            # untuk pemakai bisa mengecek data baru terlebih dahulu
            print (f'''{line2}\n\nData Baru :
    ===============================================
    family_name     : {input_cd_family_name}, 
    address         : {input_cd_address},
    telpon_number   : {input_cd_telpon_number}, 
    city            : {input_cd_city},
    code_area       : {input_cd_code_area}
    ===============================================\n
    Jika Tidak sistem akan kembali ke Halaman Utama Menu Menampilkan Data\n''')
            
            # jika pengguna mengkonfirmasi yes untuk mengubah data
            # maka data baru akan langsung di gabungkan ke data utama
            input_save_data = input ('yes / no : ' ) 
            if input_save_data == 'yes' :
                new_data = {input_cd_telpon_number : {
                'family_name' : input_cd_family_name, 
                'address' : input_cd_address,
                'telpon_number' : input_cd_telpon_number, 
                'city' : input_cd_city,
                'code_area' : input_cd_code_area}}
                yellow_pages.update(new_data)
                # sistem akan memperlihatkan data baru yang sudah digabungkan ke data utama
                print (f''' \n{line2} \n \n                                   YELLOW PAGES \n        
{'Nama Keluarga':<25}| {'Alamat':<40}| {'No Telepon':<12}| {'Kota':<20}| {'Kode Area':<10}\n{line}''')
                print (f'{yellow_pages[input_cd_telpon_number]["family_name"]:<25}| {yellow_pages[input_cd_telpon_number]["address"]:<40}| {yellow_pages[input_cd_telpon_number]["telpon_number"]:<12}| {yellow_pages[input_cd_telpon_number]["city"]:<20}| {yellow_pages[input_cd_telpon_number]["code_area"]:<10}\n{line}')
                input('\nData Sudah Tersimpan\nKlick Enter Untuk Kembali Ke Halaman Utama Menambahkan Data')
                b_menu_create_data ()
            elif input_save_data == 'no' :
                b_menu_create_data ()
            else :
                # melakukan perulangan jika konfirmasi yang diinput selain yes dan no
                # maka pengguna akan kembali untuk menginput konfirmasi ulang
                while True :
                    if input_save_data != 'yes' and input_save_data != 'no' :
                        print (f'{line2}\nINPUT YANG ANDA MASUKKAN SALAH\nMasukkan kembali input yang benar\n')
                        input_save_data = input ('Apakah Anda yakin sudah memasukkan data yang benar ?\n\nyes / no : ' )
                    else : 
                        break
        else :
            input(f'{line2}\nTIPE DATA YANG ANDA MASUKKAN SALAH\nTekan Enter untuk mengulang kembali ke MENU MENAMBAH DAFTAR YELLOW PAGES\n')
            b_menu_create_data ()
    # jika pilihan angka 2 membuat sistem kembali ke menu utama                                      
    elif pilihan_menu_create_data == '2' :
        e_main_menu ()
    # jika input salah maka akan kembali ke menu membuat data baru
    else :  
        input (f'\n{line2}\nINPUT YANG ANDA MASUKKAN SALAH\n!!! Tekan Enter untuk kembali ke MENU MENAMPILKAN DAFTAR YELLOW PAGES !!!\n')
        b_menu_create_data ()

def c_menu_update_data () :
    print (f'''{Fore.LIGHTMAGENTA_EX}{line2}
        MENU MENGUBAH DATA YELLOW PAGES\n{line2}{Style.RESET_ALL}\n
        List Menu :
        1. Mengubah Data
        2. Kembali ke Menu Utama \n
        ''')
    playsound('song 4.mp3')
    pilihan_menu_update_data = input ('Masukkan angka Menu yang ingin dijalankan : ')
    # kondisional pilihan angka
    if pilihan_menu_update_data == '1' :
        # input nomor telpon
        input_ud_telpon_number = input (f'\nMasukkan Nomor Telpon yang Ingin Diubah Datanya  : ' )
        # jika nomor tidak ada di dalam data utama
        if input_ud_telpon_number not in yellow_pages :
            input (f'{line2}\n!!! DATA YANG INGIN ANDA UBAH TIDAK ADA !!!\nTekan Enter untuk kembali ke menu update Data\n')
            c_menu_update_data ()
        # jika data ada di dalam menu utama
        # akan menunjukan baris data yg ingin diubah datanya
        elif input_ud_telpon_number in yellow_pages :
            print (f''' \n{line2} \n \n                                   YELLOW PAGES \n        
{'Nama Keluarga':<25}| {'Alamat':<40}| {'No Telepon':<12}| {'Kota':<20}| {'Kode Area':<10}\n{line}''')
            print (f'{yellow_pages[input_ud_telpon_number]["family_name"]:<25}| {yellow_pages[input_ud_telpon_number]["address"]:<40}| {yellow_pages[input_ud_telpon_number]["telpon_number"]:<12}| {yellow_pages[input_ud_telpon_number]["city"]:<20}| {yellow_pages[input_ud_telpon_number]["code_area"]:<10}\n{line}')
            # konfirmasi apakah data yang ditunjukan ingin diubah
            input_request_ud_yn = input ('\nApakah anda ingin melanjutkan untuk mengubah data ?\nJika Tidak maka sistem akan kembali ke halaman utama Menu Mengubah Data\nyes / no : ')
            if input_request_ud_yn == 'no' :
                c_menu_update_data ()
            # jika yes, akan menunjukan opsi data yg ingin diubah
            elif input_request_ud_yn == 'yes' :
                print (f'''\n{line2}\n\nPilih Kolom yang ingin diubah :\n
                       1. Nama Keluarga
                       2. Alamat
                       3. Kota
                       4. Kode Area 
                       ''')
                request_column = input ('Silahkan Masukkan nama kolom yang ingin di ubah : ')
                # peringatan jika opsi input selain 1,2,3,4
                if not request_column in ['1','2','3','4'] :
                    input (f'{line2}\n!!! OPSI YANG ANDA MASUKKAN SALAH !!!\nTekan Enter untuk kembali ke MENU MENGUBAH YELLOW PAGES ')
                    c_menu_update_data ()
                    
            else :
                while True :
                    # jika konfirmasi opsi yang diinput salah akan memberikan peringatan
                    # dan akan menyuruh pengguna untuk menginput opsi konfirmasi ulang
                    if input_request_ud_yn != 'yes' and input_request_ud_yn != 'no' :
                        print (f'{line2}\n!!! INPUT YANG ANDA MASUKKAN SALAH !!!\nMasukkan kembali input yang benar\n')
                        input_request_ud_yn = input ('Apakah anda ingin melanjutkan untuk mengubah data ?\nJika Tidak maka sistem akan kembali ke halaman utama Menu Mengubah Data\nyes / no : ')
                    else :
                        break
                  
            new_value = input ('Silahkan Masukkan data baru : ')
            input_request_column = input (f'{line2}\nApakah anda yakin data yang anda masukkan sudah benar ?\n(no) untuk kembali ke halaman utama Menu Mengubah Data\nyes / no : ')
            if input_request_column == 'no' :
                c_menu_update_data ()
            # input value baru akan dimasukkan sesuai opsi pilihan key kolom yg diinput sebelumnya
            elif input_request_column == 'yes' :
                if request_column == '1' :
                    yellow_pages[input_ud_telpon_number]['family_name'] = new_value.title()
                elif request_column == '2' :
                    yellow_pages[input_ud_telpon_number]['address'] = new_value.title()
                elif request_column == '3' :
                    yellow_pages[input_ud_telpon_number]['city'] = new_value.title()
                elif request_column == '4' :
                    # jika input value kolom code area tidak sebuah angka
                    if not new_value.isdigit() :
                        input (f'{line2}\n!!! TIPE DATA YANG ANDAMASUKKAN KE DALAM DATA BARU SALAH !!!\nTekan Enter untuk kembali ke MENU MENGUBAH DATA\n')
                        c_menu_update_data ()
                    else :
                        yellow_pages[input_ud_telpon_number]['code_area'] = new_value
                # melihatkan baris data yang sudah di update
                print (f''' \n{line2} \n \n                                   YELLOW PAGES \n        
{'Nama Keluarga':<25}| {'Alamat':<40}| {'No Telepon':<12}| {'Kota':<20}| {'Kode Area':<10}''')
                print (line)
                print (f'{yellow_pages[input_ud_telpon_number]["family_name"]:<25}| {yellow_pages[input_ud_telpon_number]["address"]:<40}| {yellow_pages[input_ud_telpon_number]["telpon_number"]:<12}| {yellow_pages[input_ud_telpon_number]["city"]:<20}| {yellow_pages[input_ud_telpon_number]["code_area"]:<10}\n{line}')
                input (f'\nData Berhasil Diubah\nTekan Enter untuk kembali ke menu update Data\n')
                c_menu_update_data ()
            # ketika input konfirmasi yes / no salah
            else :
                input (f'{line2}\n!!! INPUT YANG ANDA MASUKKAN SALAH !!!\nTekan Enter untuk kembali ke MENU MENGUBAH YELLOW PAGES\n')
                c_menu_update_data ()
    elif pilihan_menu_update_data == '2' :
        e_main_menu ()
    else :
        input (f'\n{line2}\nINPUT YANG ANDA MASUKKAN SALAH\n!!! Tekan Enter untuk kembali ke MENU MENGUBAH DAFTAR YELLOW PAGES !!!\n')
        c_menu_update_data ()

def d_menu_delete_data () :
    print (f'''{Fore.RED}{line2}
        MENU MENGHAPUS DATA YELLOW PAGES\n{line2}{Style.RESET_ALL}\n
        List Menu :
        1. Menghapus Data
        2. Kembali ke Menu Utama \n
        ''')
    playsound('song 5.mp3')
    # menghapus data dengan premary key yang di input
    pilihan_menu_dd = input ('Masukkan angka Menu yang ingin dijalankan : ')
    if pilihan_menu_dd == '1' :
        input_cd_telpon_number = input ('Silahkan Masukkan Data Nomor Telepon yang Ingin Dihapus : ' )
        # cek apakah data yg mau di hapus ada di data utama
        if input_cd_telpon_number not in yellow_pages :
            input (f'{line2}!!! Data Tidak Ada di Yellow Pages !!!\nSilahkan Enter untuk kembali ke MENU MENGHAPUS DATA YELLOW PAGES')
            d_menu_delete_data ()
        elif input_cd_telpon_number in yellow_pages :
            input_key_delate = input ('\nApakah anda yakin ingin menghapus data ini ?\nJika Tidak maka sistem akan otomatis kembali ke halaman MENU MENGHAPUS DATA YELLOW PAGES\nyes / no :')
            if input_key_delate == 'no' :
                d_menu_delete_data ()
            elif input_key_delate == 'yes' :
                del yellow_pages[input_cd_telpon_number]
                input (f'Data {input_cd_telpon_number} telah berhsil di hapus\nSilahkan klick Enter untuk kembali ke Halaman Utama Menu Menghapus Data')
                d_menu_delete_data ()
    elif pilihan_menu_dd == '2' :
        e_main_menu ()
    else :
        d_menu_delete_data ()

def menu_break () :
    input_for_break = input (f'{line2}\nApakah anda yakin, anda akan keluar ?\nyes / no : ')
    if input_for_break == 'no' :
        e_main_menu ()
    elif input_for_break == 'yes' :
        print ('Terimakasih Telah Berkunjung di Halaman Kami :D')
        playsound('song break.mp3')
    elif input_for_break != 'yes' and input_for_break != 'no' :
        input(f'{line2}\nINPUT YANG ANDA MASUKKAN SALAH\nKlick Enter Masukkan kembali input yang benar\n')
        menu_break ()
        
e_main_menu ()
                
                
            
    
    
                        
                    
                
                
                
            
    
            
            
            

        
        
        
        
    



    
