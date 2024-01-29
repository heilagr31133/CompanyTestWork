FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Set Django environment variables
ENV DJANGO_SECRET_KEY=your_secret_key
ENV DEBUG=True
ENV ALLOWED_HOSTS=localhost,127.0.0.1
ENV STRIPE_PUBLIC_KEY=pk_test_51OQer7JOA0Vjtm2XdDA0CYpoGqcioJzGlhwDAUcvFZY0vixjM4ammOh4KHrur1OFtweIQbSfqUnFCXwcI3Ra2Skv00qYoQweyv
ENV STRIPE_SECRET_KEY=sk_test_51OQer7JOA0Vjtm2XAaJPCzqwCxyLVFCYkyUgaDp6lWgZz8X2E2jU3MKEyFKCq1DBs9w3IiUn20nKcDwGQwAdWQCB00wSCtVGbk

# Run migrations and create superuser
RUN python manage.py migrate && \
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '1234')" | python manage.py shell

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
