from django.shortcuts import render
from django.http import JsonResponse
import json
import os

def add_flashcard(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        definition = request.POST.get('definition')
        
        # Create flashcards.json if it doesn't exist
        json_file_path = os.path.join(os.path.dirname(__file__), 'flashcards.json')
        
        try:
            with open(json_file_path, 'r') as f:
                flashcards = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            flashcards = []
        
        # Add new flashcard
        flashcards.append({
            'word': word,
            'definition': definition
        })
        
        # Save to JSON file
        with open(json_file_path, 'w') as f:
            json.dump(flashcards, f, indent=4)
        
        return JsonResponse({'status': 'success'})
    
    return render(request, 'flashcards/add_flashcard.html')