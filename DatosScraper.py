import requests
from bs4 import BeautifulSoup
import csv

# Lista de URLs de categorías
categories = {
    'Agua': 'https://ecotec.unam.mx/area-desarrollo/agua',
    'Alimentos': 'https://ecotec.unam.mx/area-desarrollo/alimentos',
    'Energía': 'https://ecotec.unam.mx/area-desarrollo/energia',
    'Integral': 'https://ecotec.unam.mx/area-desarrollo/integral',
    'Residuos': 'https://ecotec.unam.mx/area-desarrollo/residuos',
    'Vivienda': 'https://ecotec.unam.mx/area-desarrollo/vivienda'
}

# Abre el archivo CSV para escribir los datos
with open('ecotec_directory_all_categories3.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Categoría', 'Nombre', 'Ubicación', 'Actividad', 'Teléfono', 'Correo', 'Sitio Web', 'Link'])

    # Recorre cada categoría
    for category, url in categories.items():
        print(f'Procesando categoría: {category}')
        
        # Realiza la solicitud HTTP a la página de la categoría
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encuentra todos los elementos con la clase 'post-item'
        items = soup.find_all('div', class_='post-item')

        for item in items:
            # Extrae el nombre
            name = item.find('h5', class_='post-title').text.strip()
            
            # Extrae la URL de la página de detalles
            link = item.find('a')['href']
            if not link.startswith('http'):
                link = 'https://ecotec.unam.mx' + link
            
            # Extrae la ubicación y actividad
            text_info = item.find('div', class_='box-text-inner blog-post-inner').text.strip()
            location = text_info.split('Actividad:')[0].replace('Ubicación:', '').strip()
            activity = text_info.split('Actividad:')[1].split('Ver más')[0].strip()

            # Inicializa variables para la información adicional
            phone = ''
            email = ''
            website = ''
            
            # Realiza una solicitud a la página de detalles para obtener más información
            detail_response = requests.get(link)
            detail_soup = BeautifulSoup(detail_response.content, 'html.parser')

            # Extrae la información adicional dentro de <main>
            main_section = detail_soup.find('main')
            if main_section:
                contact_info = main_section.text.strip()
                
                # Buscar información de teléfono, correo y sitio web en el texto
                phone_start = contact_info.find('Teléfono:')
                if phone_start != -1:
                    phone = contact_info[phone_start:].split('\n')[0].replace('Teléfono:', '').strip()
                
                email_start = contact_info.find('Email:')
                if email_start != -1:
                    email = contact_info[email_start:].split('\n')[0].replace('Email:', '').strip()
                
                website_start = contact_info.find('Sitio web:')
                if website_start != -1:
                    website = contact_info[website_start:].split('\n')[0].replace('Sitio web:', '').strip()
            
            # Busca el enlace del sitio web en el HTML específico
            website_link = detail_soup.find('a', class_='vc_btn3-color-primary')
            if website_link:
                website = website_link['href'].strip()
            
            # Escribe la fila en el archivo CSV
            writer.writerow([category, name, location, activity, phone, email, website, link])

print('Scraping completado. Los datos se han guardado en ecotec_directory_all_categories3.csv')
