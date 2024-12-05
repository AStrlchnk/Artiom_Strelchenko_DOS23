# Используем официальный образ Nginx
FROM nginx:latest

# Копируем наш кастомный HTML-файл в директорию Nginx
COPY index.html /usr/share/nginx/html/index.html

# Указываем, что контейнер будет слушать порт 80
EXPOSE 80

# Запускаем Nginx
CMD ["nginx", "-g", "daemon off;"]
