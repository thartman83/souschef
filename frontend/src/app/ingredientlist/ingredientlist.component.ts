import { Component, OnInit, EventEmitter } from '@angular/core';
import { faPlus, faMinus } from '@fortawesome/free-solid-svg-icons';
import { IngredientComponent } from '../ingredient/ingredient.component';

@Component({
  selector: 'app-ingredientlist',
  templateUrl: './ingredientlist.component.html',
  styleUrls: ['./ingredientlist.component.css']
})
export class IngredientlistComponent implements OnInit {
  ingredientAdded = new EventEmitter<IngredientComponent>();
  ingredients: IngredientComponent[] = [];

  constructor() { }

  ngOnInit(): void {
  }

  faPlus = faPlus;
  faMinus = faMinus;

  onAddIngredient(): void {
    this.ingredients.push(new IngredientComponent());
  }

  deleteIngredient(i: IngredientComponent): void {
    //let ingredient = ingredients.find(e => e.id == i.id);
    i = i;
  }
}
