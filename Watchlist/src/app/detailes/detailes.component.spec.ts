import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetailesComponent } from './detailes.component';

describe('DetailesComponent', () => {
  let component: DetailesComponent;
  let fixture: ComponentFixture<DetailesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DetailesComponent]
    });
    fixture = TestBed.createComponent(DetailesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
