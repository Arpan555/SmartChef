from django.shortcuts import render,redirect
from django.views import View
from .langchain import askRecipe
from ai_chef.forms import RecipeForm

class Home(View):
    def get(self, request):
        ai_recipe = request.session.get('ai_recipe','')
        form = RecipeForm()
        return render(request, 'ai_chef/home.html',{'form':form, 'ai_recipe':ai_recipe})
    
    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe_msg = form.cleaned_data['recipe_message']
            ai_res_recipe = askRecipe(recipe_msg)
            request.session['ai_recipe'] = ai_res_recipe
        form = RecipeForm()
        return redirect('/')

