import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TmdbsearchComponent } from './tmdbsearch.component';

describe('TmdbsearchComponent', () => {
  let component: TmdbsearchComponent;
  let fixture: ComponentFixture<TmdbsearchComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TmdbsearchComponent]
    });
    fixture = TestBed.createComponent(TmdbsearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
