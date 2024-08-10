# Kurulum Talimatları

1. Paket listelerini güncelleyin:

    ```bash
    sudo apt update
    ```

2. `curl` paketini yükleyin:

    ```bash
    sudo apt install curl -y
    ```

3. `nodepay_setup.sh` scriptini indirin:

    ```bash
    curl -O https://gist.githubusercontent.com/Bo0tstrap/479627be43db165b4016291ff76ea2f1/raw/eed5ade7f5aee685db1fd50ddbe60c324e209cf8/nodepay_setup.sh
    ```

4. İndirilen script dosyasına çalıştırılabilir izin verin:

    ```bash
    chmod +x nodepay_setup.sh
    ```

5. Yeni bir `screen` oturumu başlatın:

    ```bash
    screen -S nodepay
    ```

6. Scripti belirttiğiniz URL ile çalıştırın:

    ```bash
    ./nodepay_setup.sh
    ```
7. Gerekli izini verelim:

    ```bash
    chmod +X Nodepay-cli/nodepay.py
    ```

8. Scripti çalıştır:

    ```bash
    python3 Nodepay-cli/nodepay.py
    ``` 


    

    
