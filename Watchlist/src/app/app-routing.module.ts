import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { NavbarComponent } from './navbar/navbar.component';
import { CategoryComponent } from './category/category.component';
import { DetailesComponent } from './detailes/detailes.component';
import { TmdbsearchComponent } from './tmdbsearch/tmdbsearch.component';

const routes: Routes = [
  {path:'',component:LoginComponent},
  {path:'Reg',component:SignUpComponent},
  {path:'Nav',component:NavbarComponent},
  {path:'Home',component:CategoryComponent},
  {path:'Detailes/:id',component:DetailesComponent},
  {path:'Search',component:TmdbsearchComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
