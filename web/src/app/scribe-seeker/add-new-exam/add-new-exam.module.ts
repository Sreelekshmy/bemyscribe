import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { AddNewExamPageRoutingModule } from './add-new-exam-routing.module';

import { AddNewExamPage } from './add-new-exam.page';
import { SharedModule } from 'src/app/shared/shared.module';
import { ValidationPopupComponent } from 'src/app/shared/validation-popup/validation-popup.component';

@NgModule({
  imports: [
    SharedModule,
    AddNewExamPageRoutingModule
  ],
  declarations: [
    AddNewExamPage,
    ValidationPopupComponent
  ]
})
export class AddNewExamPageModule {}
