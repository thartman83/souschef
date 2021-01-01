import { Component, OnInit, Output } from '@angular/core';
import { Recipe } from '../shared/models/recipe.model';

@Component({
  selector: 'app-createrecipe',
  templateUrl: './createrecipe.component.html',
  styleUrls: ['./createrecipe.component.css']
})
export class CreaterecipeComponent implements OnInit {
  @Output() recipe: Recipe;

  constructor() { }

  ngOnInit(): void {

  }

}
