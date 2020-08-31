import { Ingredient } from './ingredient.model';

export class IngredientList {
  constructor(public name: string, public displayorder: number,
    public ingredients: Ingredient[]) {
  }
}
