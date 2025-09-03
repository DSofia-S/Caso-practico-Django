from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics , status
from rest_framework.exceptions import NotFound
from .serializers import PersonaSerializer,TareaSerializer
from .models import Persona,Tarea
from django.shortcuts import get_object_or_404




# Create your views here.
class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    
    def get(self, request):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        if not personas:
            raise NotFound("No se encontraron personas.")
        return Response({'success': True, 'detail': 'Listado de personas', 'data': serializer.data}, status=status.HTTP_200_OK)

class CrearPersona(generics.CreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def post(self, request):
        serializer = PersonaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Persona creada con éxito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
  
class ActualizarPersona(generics.UpdateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    
    def put(self, request, pk):
        persona = get_object_or_404(Persona, pk=pk)
        email = request.data.get('email', None)
        
        if email and email != persona.email:
            if Persona.objects.filter(email=email).exclude(pk=pk).exists():
                return Response({'Email': False, 'detail': 'El email ya está en uso por otra persona.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = PersonaSerializer(persona, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Persona actualizada con éxito', 'data': serializer.data}, status=status.HTTP_200_OK)        

class PersonaByDocumento(generics.ListAPIView):
    serializer_class = PersonaSerializer

    def get(self, request, documento):
        persona= Persona.objects.filter(documento=documento).first()
        if not persona:
            raise NotFound("No se encontraron personas con ese documento.") 
        serializer= PersonaSerializer(persona)
        return Response({'success': True, 'detail': 'Persona encontrada', 'data': serializer.data}, status=status.HTTP_200_OK)

class EliminarPersona(generics.DestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def delete(self, request, pk):
        persona = get_object_or_404(Persona, pk=pk)
        persona.delete()
        return Response({'success': True, 'detail': 'Persona eliminada con éxito'}, status=status.HTTP_204_NO_CONTENT)

class TareaList(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def get(self, request):
        tareas = Tarea.objects.all()
        serializer = TareaSerializer(tareas, many=True)
        if not tareas:
            raise NotFound("No se encontraron tareas.")
        return Response({'success': True, 'detail': 'Listado de tareas', 'data': serializer.data}, status=status.HTTP_200_OK)
    
class CrearTarea(generics.CreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def post(self, request):
        serializer = TareaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Tarea creada con éxito', 'data': serializer.data}, status=status.HTTP_201_CREATED)


    serializer_class = TareaSerializer

    def get(self, request, fecha_inicio, fecha_fin):
        tareas = Tarea.objects.filter(fecha_limite__range=[fecha_inicio, fecha_fin])
        if not tareas:
            raise NotFound("No se encontraron tareas para ese rango de fechas.")
        serializer = TareaSerializer(tareas, many=True)
        return Response({'success': True, 'detail': 'Tareas encontradas', 'data': serializer.data}, status=status.HTTP_200_OK)
    
class ActualizarTarea(generics.UpdateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def put(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        serializer = TareaSerializer(tarea, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Tarea actualizada con éxito', 'data': serializer.data}, status=status.HTTP_200_OK)

class EliminarTarea(generics.DestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def delete(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        tarea.delete()
        return Response({'success': True, 'detail': 'Tarea eliminada con éxito'}, status=status.HTTP_204_NO_CONTENT)

class TareasPorFecha(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get(self, request, fecha_limite):
        tareas = Tarea.objects.filter(fecha_limite=fecha_limite).first()
        if not tareas:
            raise NotFound("No se encontraron tareas para esa fecha.")
        serializer = TareaSerializer(tareas)
        return Response({'success': True, 'detail': 'Tareas encontradas', 'data': serializer.data}, status=status.HTTP_200_OK)
    
class TareasPorPersona(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get(self, request, documento):
        tareas = Tarea.objects.filter(persona__documento=documento).first()
        if not tareas:
            raise NotFound("No se encontraron tareas para ese documento.")
        serializer = TareaSerializer(tareas)
        return Response({'success': True, 'detail': 'Tareas encontradas', 'data': serializer.data}, status=status.HTTP_200_OK)

class TareasPorRango(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get(self, request, fecha_inicio, fecha_fin):
        tareas = Tarea.objects.filter(fecha_limite__range=[fecha_inicio, fecha_fin])
        if not tareas:
            raise NotFound("No se encontraron tareas para ese rango de fechas.")
        serializer = TareaSerializer(tareas, many=True)
        return Response({'success': True, 'detail': 'Tareas encontradas', 'data': serializer.data}, status=status.HTTP_200_OK)