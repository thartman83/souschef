import { IngredientList } from './ingredientlist.model';
import { StepList } from './steplist.model';
import { Tag } from './tag.model';

export class Recipe {
  constructor(public name: string, public author: string,
    public totaltime: number, public preptime: number,
    public cooktime: number, public difficulty: number,
    public ingredientLists: IngredientList[],
    public stepLists: StepList[], public tags: Tag[]) {
  }

}
