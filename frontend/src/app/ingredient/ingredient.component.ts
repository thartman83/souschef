import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { faPlus, faMinus } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-ingredient',
  templateUrl: './ingredient.component.html',
  styleUrls: ['./ingredient.component.css']
})
export class IngredientComponent implements OnInit {
  @Output() delete: EventEmitter<IngredientComponent> = new EventEmitter();

  index: number;

  constructor() {
  }

  ngOnInit(): void {
  }

  onDelete(): void {
    this.delete.emit(this);
  }

  faPlus = faPlus;
  faMinus = faMinus;
}
