import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { RecipelistComponent } from './recipelist/recipelist.component';
import { CreaterecipeComponent } from './createrecipe/createrecipe.component';
import { IngredientlistComponent } from './ingredientlist/ingredientlist.component';
import { IngredientComponent } from './ingredient/ingredient.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    RecipelistComponent,
    CreaterecipeComponent,
    IngredientlistComponent,
    IngredientComponent
  ],
  imports: [
    BrowserModule,
    FontAwesomeModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
