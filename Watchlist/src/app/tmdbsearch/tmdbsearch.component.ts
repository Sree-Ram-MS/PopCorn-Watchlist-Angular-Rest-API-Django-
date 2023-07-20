import { Component } from '@angular/core';
import { tmdbapiservice } from '../ser/tmdbapi.service';
import { Meta, Title } from '@angular/platform-browser';
import {FormControl,FormGroup} from '@angular/forms';

@Component({
  selector: 'app-tmdbsearch',
  templateUrl: './tmdbsearch.component.html',
  styleUrls: ['./tmdbsearch.component.css']
})
export class TmdbsearchComponent {

  constructor(private service:tmdbapiservice,private title:Title,private meta:Meta) {
    this.title.setTitle('Search movies - showtime');
    this.meta.updateTag({name:'description',content:'search here movies like avatar,war etc'});
   }

  ngOnInit(): void {
  }

  searchResult:any;
  searchForm = new FormGroup({
    'movieName':new FormControl(null)
  });

  submitForm()
  {
      console.log(this.searchForm.value,'searchform#');
      this.service.getSearchMovie(this.searchForm.value).subscribe((result)=>{
          console.log(result,'searchmovie##');
          this.searchResult = result.results;
      });
  }

}
