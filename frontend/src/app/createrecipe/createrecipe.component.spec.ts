import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { CreaterecipeComponent } from './createrecipe.component';

describe('CreaterecipeComponent', () => {
  let component: CreaterecipeComponent;
  let fixture: ComponentFixture<CreaterecipeComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ CreaterecipeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreaterecipeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
